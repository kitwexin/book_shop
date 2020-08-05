from django.urls import path
from . import views
app_name = 'authors'

urlpatterns = [
    path('create-author/', views.AuthorCreateView.as_view(), name = 'create'),
    path('list-authors/', views.AuthorListView.as_view(), name = 'list'),
    path('update-author/<int:pk>', views.AuthorUpdateView.as_view(), name = 'update'),
    path('delete-author/<int:pk>', views.AuthorDeleteView.as_view(), name = 'delete'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name = 'detail')
]