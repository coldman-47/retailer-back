from django.urls import path
from revendeurBackOffice import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('products/edit', views.UpdateProduct.as_view())
]