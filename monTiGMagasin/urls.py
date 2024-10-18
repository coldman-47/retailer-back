from django.urls import path
from monTiGMagasin import views

urlpatterns = [
    path('infoproducts/', views.InfoProductList.as_view()),
    path('infoproduct/<int:tig_id>/', views.InfoProductDetail.as_view()),
    path('infoproduct/putonsale/<int:tig_id>/<str:new_price>/', views.PutProductOnSale.as_view()),
    path('infoproduct/removesale/<int:tig_id>/', views.RemoveOnSale.as_view()),
    path('infoproduct/incrementStock/<int:tig_id>/<int:number>/', views.IncrementStock.as_view()),
    path('infoproduct/decrementStock/<int:tig_id>/<int:number>/', views.DecrementStock.as_view()),
    path('infoproducts/updatesales/', views.UpdateSales.as_view()),
]
