# Generated by Django 4.2.3 on 2023-08-04 11:18

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Категория товаров',
                'verbose_name_plural': 'Категории товаров',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, null=True, verbose_name='Название')),
                ('slug', models.SlugField(default='-', max_length=300, verbose_name='Слаг для url')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('discription', models.TextField(blank=True, help_text='Дополнительная информация о товаре, его характерестиках и свойствах.', verbose_name='Описание')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('archived', models.BooleanField(default=False, help_text='Будет ли слово отображаться в каталоге?', verbose_name='Архивировано')),
                ('img', models.ImageField(blank=True, null=True, upload_to='for_products', verbose_name='Изображение')),
                ('category', models.ForeignKey(help_text='Группа товара, по которой будет фильтроваться их список.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categ_products', to='products.category', verbose_name='Категория')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_products', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['add_date', 'name'],
                'indexes': [models.Index(fields=['-add_date'], name='products_pr_add_dat_8d71f7_idx')],
            },
        ),
    ]
