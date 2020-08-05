from django.urls import path
from . import views
app_name = 'cart'

urlpatterns = [
    path('add/', views.AddBookToCart.as_view(), name = 'add'),
    path('cart/', views.CartDetail.as_view(), name = 'cart'),
    path('delete/<int:pk>', views.ProductInCartDelete.as_view(), name = 'delete'),
]