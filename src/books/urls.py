from django.urls import path
from . import views
app_name = 'books'

urlpatterns = [
    path('create-book/', views.BooksCreateView.as_view(), name = 'create'),
    path('list-books/', views.BooksListView.as_view(), name = 'list'),
    path('update-book/<int:pk>', views.BooksUpdateView.as_view(), name = 'update'),
    path('delete-book/<int:pk>', views.BooksDeleteView.as_view(), name = 'delete'),
    path('book/<int:pk>', views.BooksDetailView.as_view(), name = 'detail')
]