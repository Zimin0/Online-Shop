from django.contrib import admin
from products.models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'price', 'discription', 'category', 'seller', 'add_date') # эти поля отображаются в строке экземпляра
    list_filter = ( 'category', 'seller', 'add_date', 'archived') # фильтрация по этим полям
    search_fields = ('name', 'discription', ) # поиск по этим полям
    prepopulated_fields = {'slug': ('name',)} # предзаполнит поле slug текстом из name
    raw_id_fields = ('seller',) # поле автора будет не выпадающим списком, а полем поиска
    date_hierarchy = 'add_date' # под полем поиска ссылки на временные периоды

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)