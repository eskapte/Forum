from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')
    close_time = models.DateTimeField(verbose_name='Дата закрытия', blank=True, null=True, default=None)
    rubric = models.ForeignKey('Rubric', on_delete=models.PROTECT, verbose_name='Рубрика')

    statuses = [
        ('o', 'Открыт'),
        ('c', 'Закрыт')
    ]

    status = models.CharField(max_length=10, choices=statuses, default='o', verbose_name='Статус')
    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_icon = models.ImageField(upload_to='Lamersroom/images/', blank=True, null=True,
                                  verbose_name='Аватар', default='Lamersroom/images/default_icon.jpg')
    user_status = models.CharField(max_length=50, verbose_name='Статус', blank=True, null=True)
    user_about = models.TextField(verbose_name='О себе', max_length=300, blank=True, null=True)
    first_name = models.CharField(max_length=30, verbose_name='Имя', blank=True, null=True)
    last_name = models.CharField(max_length=30, verbose_name='Фамилия', blank=True, null=True)
    respect = models.IntegerField(verbose_name='Репутация', default=0)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

    def __str__(self):
        return self.user.username


class Rubric(models.Model):
    name = models.CharField('Рубрика', max_length=50)

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост')
    content = models.TextField(max_length=500)
    add_time = models.DateTimeField(verbose_name='Добавлен', auto_now_add=True, editable=False)
    comment_author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор комментария', default=None)
    likes = models.IntegerField(verbose_name='Лайки', default=0)

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['-add_time']
