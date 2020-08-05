from django.urls import path
from . import views
app_name = 'order'

urlpatterns = [
    path('create/', views.CreateOrder.as_view(), name = 'create'),
    path('done/', views.OrderDone.as_view(), name = 'done'),
    path('done2/', views.OrderDone2.as_view(), name = 'done2'),
    path('list/', views.OrderListView.as_view(), name = 'list'),
    path('detail/<int:pk>', views.OrderDetailView.as_view(), name = 'detail'),
    path('delete/<int:pk>', views.OrderDeleteView.as_view(), name = 'delete')
]