from django import template
from news_portal.models import Subscribers, Category
from django.http import HttpResponse

register = template.Library()


@register.simple_tag
def subscribe_me1(request):
    user = request.user
    post_category = Category.objects.filter(id=1)[0]
    if Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).exists():
        Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).delete()
        response = HttpResponse()
        response.write(f"<p>Вы отписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response
    else:
        Subscribers.objects.create(user_id=user.id, category_id=post_category.id)
        response = HttpResponse()
        response.write(f"<p>Вы подписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response


@register.simple_tag
def subscribe_me2(request):
    print(request)
    user = request.user
    post_category = Category.objects.filter(id=2)[0]
    if Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).exists():
        Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).delete()
        response = HttpResponse()
        response.write(f"<p>Вы отписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response
    else:
        Subscribers.objects.create(user_id=user.id, category_id=post_category.id)
        response = HttpResponse()
        response.write(f"<p>Вы подписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response


@register.simple_tag
def subscribe_me3(request):
    print(request)
    user = request.user
    post_category = Category.objects.filter(id=3)[0]
    if Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).exists():
        Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).delete()
        response = HttpResponse()
        response.write(f"<p>Вы отписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response
    else:
        Subscribers.objects.create(user_id=user.id, category_id=post_category.id)
        response = HttpResponse()
        response.write(f"<p>Вы подписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response


@register.simple_tag
def subscribe_me4(request):
    print(request, id)
    user = request.user
    post_category = Category.objects.filter(id=4)[0]
    if Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).exists():
        Subscribers.objects.filter(user_id=user.id, category_id=post_category.id).delete()
        response = HttpResponse()
        response.write(f"<p>Вы отписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response
    else:
        Subscribers.objects.create(user_id=user.id, category_id=post_category.id)
        response = HttpResponse()
        response.write(f"<p>Вы подписались на новости в категории {post_category.name}</p>")
        response.write('<a class="nav-link" href="/news/search/">Вернуться</a>')
        return response
