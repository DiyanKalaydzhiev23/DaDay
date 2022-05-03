from django.urls import path
from server.auth_app.views import UserCreate, LoginUserView, ProfileView
from .signals import *


urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/<int:user_id>', ProfileView.as_view(), name='profile'),
]
