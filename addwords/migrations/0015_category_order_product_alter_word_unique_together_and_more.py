# Generated by Django 4.1.6 on 2023-04-05 14:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('addwords', '0014_alter_exchange_from_user_alter_exchange_to_user_and_more'),
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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('IN', 'In progress'), ('RE', 'Rejected'), ('FI', 'Finished')], default='IN', max_length=30)),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanges_from', to=settings.AUTH_USER_MODEL, verbose_name='От пользователя')),
            ],
            options={
                'verbose_name': 'Заказ пользователя',
                'verbose_name_plural': 'Заказы пользователей',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, null=True, verbose_name='Название')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('discription', models.TextField(blank=True, help_text='Дополнительная информация о товаре, его характерестиках и свойствах.', verbose_name='Описание')),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(help_text='Группа товара, по которой будет фильтроваться их список.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categ_products', to='addwords.category', verbose_name='Категория')),
                ('saller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_products', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='word',
            name='author',
        ),
        migrations.RemoveField(
            model_name='word',
            name='language',
        ),
        migrations.RemoveField(
            model_name='word',
            name='synonyms',
        ),
        migrations.RemoveField(
            model_name='advuser',
            name='is_activated',
        ),
        migrations.AddField(
            model_name='advuser',
            name='is_saller',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Exchange',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(help_text='Товары, составляющие заказ.', to='addwords.product', verbose_name='Товары'),
        ),
        migrations.AddField(
            model_name='order',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exchanges_to', to=settings.AUTH_USER_MODEL, verbose_name='Пользователю'),
        ),
    ]
