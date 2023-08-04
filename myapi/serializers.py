from rest_framework import serializers

from products.models import Product, Category

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.CharField(source="category.name")
    seller = serializers.CharField(source="seller.username")
    class Meta:
        model = Product
        fields = ('name', 'price', 'category', 'seller', 'add_date', 'archived', 'img')

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)