from django.contrib.auth import get_user_model
from rest_framework import permissions, generics
from rest_framework.views import APIView
from server.auth_app.serializers import UserSerializer


UserModel = get_user_model()


class UserCreate(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

