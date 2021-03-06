from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework import viewsets

# Create your views here.

class LargeResultsSetPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 10000

class KiyimlarViewSet(viewsets.ModelViewSet):
    queryset = Kiyimlar.objects.all()
    serializer_class = KiyimlarSerializer
    pagination_class = LargeResultsSetPagination
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','price']
    ordering = ['price']
    search_fields = ['^name']
    filterset_fields = ['name','price']
    # pagination_class = LimitOffsetPagination

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AloqaViewSet(viewsets.ModelViewSet):
    queryset = Aloqa.objects.all()
    serializer_class = AloqaSerializer
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','subject']
    ordering = ['subject']
    search_fields = ['^name','subject']
    filterset_fields = ['name','subject']

class CardItemViewSet(viewsets.ModelViewSet):
    queryset = CardItem.objects.all()
    serializer_class = CardItemSerializer        
    permission_classes = [IsAuthenticated]
    
class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]