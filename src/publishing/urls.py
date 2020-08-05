from django.urls import path
from . import views
app_name = 'publishing'

urlpatterns = [
    path('create-publishing/', views.PublishingCreateView.as_view(), name = 'create'),
    path('list-publishing/', views.PublishingListView.as_view(), name = 'list'),
    path('update-publishing/<int:pk>', views.PublishingUpdateView.as_view(), name = 'update'),
    path('delete-publishing/<int:pk>', views.PublishingDeleteView.as_view(), name = 'delete'),
    path('publishing/<int:pk>', views.PublishingDetailView.as_view(), name = 'detail')
]