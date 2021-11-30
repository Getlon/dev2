from django.contrib.auth.models import User
from project.news_portal.models import Author, Category, Post, PostCategory, Comment


#1
dima_user = User.objects.create_user(username='dima', email='dima@mail.ru', password='dima_password')
vasya_user = User.objects.create_user(username='vasya', email='vasya@mail.ru', password='vasya_password')

#2
dima_author = Author.objects.create(user=dima_user)
vasya_author = Author.objects.create(user=vasya_user)

#3
sport = Category.objects.create(name='sport')
music = Category.objects.create(name='music')
science = Category.objects.create(name='science')
cinema = Category.objects.create(name='cinema')

#4
news_dima = Post.objects.create(author=dima_author, form=Post.news, headline="новость_dima", text='Дима новость jfbrgfuvhdfnfbdjf')
article_dima = Post.objects.create(author=dima_author, form=Post.article, headline="статья_dima", text='Дима статья kfouiryetr6537r336')
article_vasya = Post.objects.create(author=vasya_author, form=Post.article, headline="новость_vasya", text='Вася статья 3973843648346383473')

#5
PostCategory.objects.create(post=news_dima, category=sport)
PostCategory.objects.create(post=news_dima, category=cinema)
PostCategory.objects.create(post=article_dima, category=cinema)
PostCategory.objects.create(post=article_dima, category=science)
PostCategory.objects.create(post=article_vasya, category=music)
PostCategory.objects.create(post=article_vasya, category=sport)

#6
comment1 = Comment.objects.create(post=news_dima, user=vasya_user, text='1 коммент Васи Диме')
comment2 = Comment.objects.create(post=article_dima, user=vasya_user, text='2 коммент Васи Диме')
comment3 = Comment.objects.create(post=article_vasya, user=dima_user, text='3 коммент Димы Васе')
comment4 = Comment.objects.create(post=article_vasya, user=dima_user, text='4 коммент Димы Васе')

#7
comment1.like()
comment1.like()
comment3.dislike()
comment3.dislike()
news_dima.like()
news_dima.like()
news_dima.like()
article_vasya.dislike()
article_vasya.dislike()
article_vasya.dislike()

#8
raiting_dima = (sum([post.rating*3 for post in Post.objects.filter(author=dima_author)])
                + sum([comment.rating for comment in Comment.objects.filter(user=dima_user)])
                + sum([comment.rating for comment in Comment.objects.filter(post__author=dima_author)])
                )
dima_author.update_rating(raiting_dima)

raiting_vasya = (sum([post.rating*3 for post in Post.objects.filter(author=vasya_author)])
                + sum([comment.rating for comment in Comment.objects.filter(user=vasya_user)])
                + sum([comment.rating for comment in Comment.objects.filter(post__author=vasya_author)])
                )
vasya_author.update_rating(raiting_vasya)

#9
best_author = Author.objects.all().order_by('-rating')[0]
print()
print(f'Лучший автор username: {best_author.user.username}, raiting: {best_author.rating}')
print()

#10
best_article = Post.objects.filter(form=Post.article).order_by('-rating')[0]
print()
print('Лучшая статья:')
print(best_article.publication_date_and_time)
print(best_article.author.user.username)
print(best_article.rating)
print(best_article.headline)
print(best_article.preview())
print()

#11
print("Комментарии к лучшей статье:")
for comment in Comment.objects.filter(post=best_article):
    print()
    print(comment.comment_date_and_time)
    print(comment.user)
    print(comment.text)
    print()
