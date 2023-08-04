from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Order(models.Model):
    STATUS = (
        (None, "Choose "), # или None -  заменяет --------- на "Choose order status"
        ('IN', 'In progress'),
        ('RE', 'Rejected'),
        ('FI', 'Finished')
    )
    
    products = models.ManyToManyField(Product, blank=False, verbose_name="Товары", help_text="Товары, составляющие заказ.") # , related_name='+'
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="От пользователя", related_name='exchanges_from') 
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователю", related_name='exchanges_to')
    date = models.DateTimeField(auto_now_add=True)
    stage_status = models.CharField(max_length=30, choices=STATUS, default='IN')

    def get_readable_status(self) -> str:
        """ Возвращает читаемый статус заказа из STATUS """
        for trpl in self.STATUS:
            if self.stage_status == trpl[0]:
                return trpl[1]
        return ''  
    
    def __str__(self):
        return f"{self.from_user} --> {self.to_user}" 
    
    class Meta:
        verbose_name = "Заказ пользователя"
        verbose_name_plural = "Заказы пользователей"