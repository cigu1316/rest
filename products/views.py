from django.shortcuts import render
from rest_framework.generics import ListAPIView


class ProductsListAPIView(ListAPIView):
    def get_queryset(self):
        return Products.objects.all()

    def get_serializer_class(self):
        return ProductsSerializer

    
   

    