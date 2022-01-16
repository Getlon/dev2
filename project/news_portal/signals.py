from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save, m2m_changed
from .models import Post, Subscribers, User, ForScheduler
from django.db import transaction
import django
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from project.settings import DEFAULT_FROM_EMAIL


@receiver(m2m_changed, sender=Post.category.through)
def notify_about_new_news(sender, instance, action, **kwargs):
    if action == 'post_add':
        print('post_add сработал')
        category_id_list = [category.id for category in instance.category.all()]
        user_id_list = []
        for category_id in category_id_list:
            for obj in Subscribers.objects.filter(category_id=category_id):
                if obj.user_id not in user_id_list:
                    user_id_list.append(obj.user_id)
        email_list = []
        username_list = []
        for id in user_id_list:
            if User.objects.filter(id=id)[0].email not in email_list:
                email_list.append(User.objects.filter(id=id)[0].email)
            if User.objects.filter(id=id)[0].username not in username_list:
                username_list.append(User.objects.filter(id=id)[0].username)

        for email, id in zip(email_list, user_id_list):
            try:
                ForScheduler.objects.create(email=email, link=f'http://127.0.0.1:8000/news/{instance.id}/, ', user_id=id)
            except transaction.atomic():
                obj = ForScheduler.objects.filter(email=email)[0]
                obj.link = obj.link.replace(f'http://127.0.0.1:8000/news/{instance.id}/, ', '')
                obj.link = obj.link + f'http://127.0.0.1:8000/news/{instance.id}/, '
                obj.save()
                continue
        print(category_id_list)

    # for us, em in zip(username_list, email_list):
    #     subject = f'Здравствуй, {us}. Новая статья в твоём любимом разделе!'
    #     body = f'Заголовок {instance.headline}' \
    #            f'Ссылка на новость http://127.0.0.1:8000/news/{instance.id}/' \
    #            f'Краткое содержание{instance.preview()}'
    #     html_save = render_to_string('post_changes_create.html', {'post': instance})
    #     msg = EmailMultiAlternatives(subject, body, DEFAULT_FROM_EMAIL, to=[em, ])
    #     msg.attach_alternative(html_save, "text/html")  # добавляем html
    #     msg.send()  # отсылаем
