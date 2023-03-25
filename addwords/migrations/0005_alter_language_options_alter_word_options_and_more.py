# Generated by Django 4.1.6 on 2023-03-25 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addwords', '0004_alter_language_options_alter_word_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='language',
            options={'verbose_name': 'Язык', 'verbose_name_plural': 'Языки'},
        ),
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['word', 'type'], 'verbose_name': 'Слово', 'verbose_name_plural': 'Слова'},
        ),
        migrations.AlterUniqueTogether(
            name='word',
            unique_together={('word', 'language'), ('word', 'type', 'translation')},
        ),
    ]
