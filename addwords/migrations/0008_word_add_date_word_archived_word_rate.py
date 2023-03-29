# Generated by Django 4.1.6 on 2023-03-25 18:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('addwords', '0007_alter_word_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='add_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='word',
            name='archived',
            field=models.BooleanField(default=False, help_text='Будет ли слово отображаться в словаре?', verbose_name='Архивировано'),
        ),
        migrations.AddField(
            model_name='word',
            name='rate',
            field=models.IntegerField(default=5, help_text='Личный рейтинг слова от 1 до 10', verbose_name='Рейтинг'),
        ),
    ]