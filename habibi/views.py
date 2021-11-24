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

class KiyimlarPageNumberPaginations(PageNumberPagination):
    page_size = 3


class KiyimlarViewSet(viewsets.ModelViewSet):
    queryset = Kiyimlar.objects.all()
    serializer_class = KiyimlarSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    filter_backends = [filters.OrderingFilter,DjangoFilterBackend,filters.SearchFilter]
    ordering_fields = ['name','price']
    ordering = ['price']
    search_fields = ['^name']
    filterset_fields = ['name','price']
