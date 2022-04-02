from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('server.da_day.urls')),
    path('api-auth/', include('rest_framework.urls')),
]
