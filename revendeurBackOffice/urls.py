from django.urls import path
from revendeurBackOffice import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('products', views.ProductList.as_view()),
    path('product/<int:pk>', views.ProductDetails.as_view()),
    path('products/edit', views.UpdateProduct.as_view()),
    path('operations', views.OperationList.as_view()),
    path('operation', views.AddOperation.as_view()),
    path('operation/<int:pk>', views.UpdateOperation.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', views.Registration.as_view(), name='register')
]
