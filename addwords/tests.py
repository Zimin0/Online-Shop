from django.test import TestCase
from django.contrib.auth.models import User 
from .models import Product, Category
import random

categories = []
users = []
for cat in range(5):
    c = Category.objects.create(name=f'Категория №{cat}')
    c.save()
    categories.append(c)

    u = User.objects.create_user(username=f"user{cat}", email=f"user{cat}@gmail.com", password=f"user{cat}")
    u.save()
    users.append(u)


for pro in range(5*100):
    p = Product.objects.create(
        name=f"Продукт №{pro}",
        price=random.randint(100,5000),
        discription="Описание товара. Содержит подробную информацию о товаре и его характеристиках. Описывает свойства и положительные стороны. Подтверждает данную стоимость товара.",
        category=random.choice(categories),
        seller=random.choice(users),
    )
    p.save()