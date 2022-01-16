import logging

from news_portal.models import ForScheduler
from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from project.settings import DEFAULT_FROM_EMAIL

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution

logger = logging.getLogger(__name__)


# наша задача по выводу текста на экран
def my_job():
    username_list = []
    email_list = []
    link_list = []
    for obj in ForScheduler.objects.all():
        username_list.append(User.objects.filter(id=obj.user_id)[0])
        email_list.append(obj.email)
        link_list.append(obj.link)

    for us, em, link in zip(username_list, email_list, link_list):
        subject = f'Здравствуй, {us}. Недельный отчет об новых статьях!'
        body = f'Ссылки на новости {link}'
        html_save = render_to_string('post_changes_create.html')
        msg = EmailMultiAlternatives(subject, body, DEFAULT_FROM_EMAIL, to=[em, ])
        msg.attach_alternative(html_save, "text/html")  # добавляем html
        msg.send()  # отсылаем

    ForScheduler.objects.all().delete()


# функция, которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(week="*/1"),
            # То же, что и интервал, но задача тригера таким образом более понятна django
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),
            # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")
