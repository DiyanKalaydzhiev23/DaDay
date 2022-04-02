from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('server.da_day.urls')),
    path('auth/', include('server.auth_app.urls')),
    path('api-token-auth/', views.obtain_auth_token),
]
