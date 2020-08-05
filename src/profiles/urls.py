from django.urls import path
from . import views
app_name = 'profiles'

urlpatterns = [
    path('update/<int:user_pk>', views.ProfileUpdate.as_view(), name = 'update'),
    path('create-user/', views.CreateUser.as_view(), name = 'create-user')
]