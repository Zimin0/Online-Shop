from rest_framework import viewsets
from .serializers import ProductSerializer, CategorySerializer
from addwords.models import Product, Category


class ProductViewSet(viewsets.ModelViewSet):
    """ Он будет обрабатывать GET и POST для Heroe без дополнительной работы. """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
