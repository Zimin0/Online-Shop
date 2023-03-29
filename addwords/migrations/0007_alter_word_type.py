# Generated by Django 4.1.6 on 2023-03-25 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addwords', '0006_alter_word_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='type',
            field=models.CharField(blank=True, choices=[(None, 'Выберите тип слова'), ('Verb', 'Verb (сущ.)'), ('Noun', 'Noun (глаг.)'), ('Adjective', 'Adjective (прил.)')], max_length=10),
        ),
    ]