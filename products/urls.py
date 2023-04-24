from django.urls import path

from products.views import ProductsListAPIView

urlpatterns = [
   
    path('products/', ProductsListAPIView.as_view(), name='products-list-view'),
   

]