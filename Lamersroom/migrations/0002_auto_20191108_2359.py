# Generated by Django 2.2.2 on 2019-11-08 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Lamersroom', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='close_time',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Дата закрытия'),
        ),
    ]
