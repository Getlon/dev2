from django.forms import ModelForm, BooleanField
from .models import Post
from django import forms


class PostForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строиться форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    check_box = BooleanField(label='Ало, Галочка!')

    class Meta:
        model = Post
        fields = ['author', 'category', 'form', 'headline', 'text', 'check_box']
