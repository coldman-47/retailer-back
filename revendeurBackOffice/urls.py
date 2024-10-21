from django.urls import path
from revendeurBackOffice import views

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view()),
    path('products/edit', views.UpdateProduct.as_view()),
    path('operations', views.OperationList.as_view()),
    path('operation', views.AddOperation.as_view())
]