from django.urls import path
from server.auth_app.views import UserCreate


urlpatterns = [
    path('register/', UserCreate.as_view(), name='register'),
]
