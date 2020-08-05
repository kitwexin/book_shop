from django.urls import path
from . import views
app_name = 'genres'

urlpatterns = [
    path('create-genre/', views.GenreCreateView.as_view(), name = 'create'),
    path('list-genres/', views.GenreListView.as_view(), name = 'list'),
    path('update-genre/<int:pk>', views.GenreUpdateView.as_view(), name = 'update'),
    path('delete-genre/<int:pk>', views.GenreDeleteView.as_view(), name = 'delete'),
    path('genre/<int:pk>', views.GenreDetailView.as_view(), name = 'detail')
]