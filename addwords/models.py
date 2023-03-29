from django.db import models
from django.contrib.auth.models import User

class Word(models.Model):
    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
        unique_together = (('word', 'language'), # уникальные сочетания полей в модели
                           (('word', 'type', 'translation')))
        ordering = ['word', 'type'] # параметры сортировки записей по умолчанию

    TYPE = (
        (None, "Выберите тип слова"), # или None -  заменяет --------- на Выберите тип слова
        ('Verb', 'Verb (сущ.)' ),
        ('Noun', 'Noun (глаг.)'),
        ('Adjective', 'Adjective (прил.)'),
    )

    word = models.CharField(max_length=20, null=True, blank=False, verbose_name="Слово")
    language = models.ForeignKey("Language", on_delete=models.PROTECT, verbose_name="Язык", related_name='words') #, limit_chices_to={}
    # если related_name не указан, то будет равен Word_set
    type = models.CharField(max_length=10, choices=TYPE, blank=True)
    translation = models.CharField(max_length=25, verbose_name="Перевод")
    discription = models.TextField(blank=True, verbose_name="Доп. комментарий к переводу")
    synonyms = models.ManyToManyField("Word", verbose_name="Синонимы", related_name='+', blank=True)
    rate = models.IntegerField(verbose_name="Рейтинг", default=5, help_text="Личный рейтинг слова от 1 до 10")
    add_date = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True, blank=True)
    archived = models.BooleanField(verbose_name="Архивировано", help_text="Будет ли слово отображаться в словаре?", default=False)
    author =  models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="Автор", help_text="Кто добавил слово", blank=True, null=True, related_name='user_words')
    img = models.ImageField(upload_to="for_words", null=True, blank=True, verbose_name="Изображение", help_text='Картинка, которая поможеть запомнить слово.')

    def __str__(self):
        return self.word
    
    def get_synonyms(self):
        return [s.__str__() for s in self.synonyms.all()]


# Свзяь один с одим - Для объединения  двух моделей, одна из которых хранит данные о другой
# auto_now - заносится текущая дата при изменении и сохранении записи - исользовать как дату последнего изменения
# auto_now_add - заносится при создании и при последующих сохранениях - для даты создания записи
# editable - False - не будет выводиться в админке
# primary_key - ключевое поле, обязательно к заполнению и уникально. Должно быть только одно в модели
# null - если True, то в поле бд может храниться значение null, иначе поле должно иметь хоть какое-то значение, даже пустую строку.
# ForeignKey - если нужно создать рекрсивную связь, то первым параметром указываем 'self' - ForeignKey('self', on_delete=...)

class Language(models.Model):

    class Meta:
        verbose_name = "Язык"
        verbose_name_plural = "Языки"

    name =  models.CharField(max_length=30, null=True, blank=False, verbose_name="Язык")

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        print("Запись language сохранена!") # заменить на log
        super().save(*args, **kwargs)
    
    


class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True) # изначально это поле содержит None
    user = models.OneToOneField(User, on_delete=models.CASCADE)

