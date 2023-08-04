from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=40, null=True, blank=False, verbose_name="Название")
    
    def __str__(self):
        return self.name

    def name_with_quotes(self):
        """ Используется для вывода вы шаблоне"""
        return f'"{self.name}"'

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"

class PublishedManager(models.Manager):
    """ 
    Модальный менеджер, как objects. \n
    Вызывается: Product.published.all() \n
    Выводит все товары со статусом archived = False
    """
    def get_queryset(self):
        return super().get_queryset().filter(archived=False)


class Product(models.Model):
    name = models.CharField(max_length=400, null=True, blank=False, verbose_name="Название")
    slug = models.SlugField(max_length=300, verbose_name="Слаг для url", blank=False)
    price = models.IntegerField(verbose_name="Цена", default=0)
    discription = models.TextField(blank=True, verbose_name="Описание", help_text="Дополнительная информация о товаре, его характерестиках и свойствах.")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="categ_products", verbose_name="Категория", help_text="Группа товара, по которой будет фильтроваться их список.")
    seller = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец", related_name='user_products')
    add_date = models.DateTimeField(auto_now_add=True)
    archived = models.BooleanField(verbose_name="Архивировано", help_text="Будет ли слово отображаться в каталоге?", default=False)
    img = models.ImageField(upload_to="for_products", null=True, blank=True, verbose_name="Изображение")
    
    objects = models.Manager()  # менеджер по умолчанию
    published = PublishedManager()  # менеджер, выводящий неархивированные товары

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        print("Запись Product сохранена!")
        super().save(*args, **kwargs)

    def get_add_date(self):
        return f"Добавлен {self.add_date}"

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        indexes = [models.Index(fields=['-add_date'])]  # Добавляет индекс в базу данных - ускоряет запросы, фильтрующие и упорядочивающие по данному полю
        ordering = ['add_date', 'name']  # параметры сортировки записей по умолчанию
        # unique_together = (('name', 'price'), ('discription', 'category', 'seller'))
