from django.contrib import admin
from .models import Category, Product, Order


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discription', 'category', 'seller', 'add_date') # эти поля отображаются в строке экземпляра
    list_filter = ('name', 'category', 'seller', 'add_date', 'archived') # фильтрация по этим полям
    search_fields = ('name', 'discription', ) # поиск по этим полям

class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'from_user', 'to_user', 'date', 'status')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)