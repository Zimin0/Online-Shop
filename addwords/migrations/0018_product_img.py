# Generated by Django 4.1.6 on 2023-04-05 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addwords', '0017_product_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='for_products', verbose_name='Изображение'),
        ),
    ]
