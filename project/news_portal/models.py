from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self, new_rating):
        self.rating = new_rating
        self.save()


class ForScheduler(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50, unique=True)
    link = models.TextField()

    def __str__(self):
        return f'{self.id}, {self.email}, {self.link}, {self.user}'


class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)


class Subscribers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')
    article = 'article'
    news = 'news'
    list1 = [(article, 'Статья'), (news, 'Новость')]
    form = models.CharField(choices=list1, default=news, max_length=7)
    publication_date_and_time = models.DateTimeField(auto_now_add=True)
    headline = models.CharField(max_length=128)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return self.text[:125] + '...'

    def __str__(self):
        return f'{self.headline} preview: {self.text[:20]}'

    def get_category_names(self):
        result = []
        for category in self.category.all():
            result.append(category.name)
        return ', '.join(result)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    comment_date_and_time = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
