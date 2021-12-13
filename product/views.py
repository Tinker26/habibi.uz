from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCategoryViewSet(viewsets.ModelViewSet):
    queryset = Categorya.objects.all()
    serializer_class = ProductCategorySerializer

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer        

class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer