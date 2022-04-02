from django.contrib.auth import get_user_model
from rest_framework import permissions, generics, status
from rest_framework.response import Response

from server.auth_app.serializers import UserSerializer
from rest_framework.authtoken.models import Token


UserModel = get_user_model()


class UserCreate(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

