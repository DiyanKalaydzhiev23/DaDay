from django.urls import path
from server.auth_app.views import UserCreate, LoginUserView, ProfileView, ResetPasswordTokenView, NewPasswordView
from .signals import *


urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('profile/<int:user_id>', ProfileView.as_view(), name='profile'),
    path('send-token/<str:email>', ResetPasswordTokenView.as_view(), name='send token'),
    path('reset-password/<int:user_id>', NewPasswordView.as_view(), name='new password'),
]
