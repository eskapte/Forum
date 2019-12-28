# Generated by Django 2.2.2 on 2019-10-24 18:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rubric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Рубрика',
                'verbose_name_plural': 'Рубрики',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_icon', models.ImageField(blank=True, default='Lamersroom/images/default_icon.jpg', null=True, upload_to='Lamersroom/images/', verbose_name='Аватар')),
                ('user_status', models.CharField(blank=True, max_length=50, null=True, verbose_name='Статус')),
                ('user_about', models.TextField(blank=True, max_length=300, null=True, verbose_name='О себе')),
                ('first_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=30, null=True, verbose_name='Фамилия')),
                ('respect', models.IntegerField(default=0, editable=False, verbose_name='Репутация')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('text', models.TextField(verbose_name='Описание')),
                ('published', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('close_time', models.DateTimeField(blank=True, default=None, editable=False, null=True, verbose_name='Дата закрытия')),
                ('status', models.CharField(choices=[('o', 'Открыт'), ('c', 'Закрыт')], default='o', max_length=10, verbose_name='Статус')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('rubric', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Lamersroom.Rubric', verbose_name='Рубрика')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
                'ordering': ['-published'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('add_time', models.DateTimeField(auto_now_add=True, verbose_name='Добавлен')),
                ('comment_author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Lamersroom.Post', verbose_name='Пост')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-add_time'],
            },
        ),
    ]
