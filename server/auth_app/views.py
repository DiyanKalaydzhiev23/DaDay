from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.hashers import make_password
from rest_framework import generics, status, views
from rest_framework.response import Response
from server.auth_app.models import Profile, ResetPasswordData
from server.auth_app.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from server.auth_app.tasks import handle_reset_password, delete_reset_password_token
from server.common.helpers import authenticated_user

UserModel = get_user_model()


class UserCreate(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        token, created = Token.objects.get_or_create(user=serializer.instance)

        user = UserModel.objects.get(username=serializer.data['username'])
        profile = Profile.objects.get(user_id=user.id)

        return Response(
            {
                'token': token.key,
                'user_id': user.id,
                'username': user.username,
                'avatar': profile.avatar
            },
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class LoginUserView(views.APIView):
    queryset = UserModel.objects.all()

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        check_user = UserModel.objects.filter(username=username)
        if not check_user:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=request.user)
            profile = Profile.objects.get(user_id=user.id)

            data = {
                'token': token.key,
                'user_id': request.user.pk,
                'username': request.user.username,
                'avatar': profile.avatar,
            }

            return Response(data, status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_400_BAD_REQUEST)


class ProfileView(views.APIView):
    def get(self, request, user_id, user_to_show_id):
        authenticated_user(request, user_id)

        context = {
            "is_owner": True if user_id == user_to_show_id else False,
            "user": UserSerializer(UserModel.objects.get(pk=user_to_show_id)).data,
            "id": user_to_show_id,
        }

        return Response(context, status=status.HTTP_200_OK)


class ResetPasswordTokenView(views.APIView):
    def get(self, request, email):
        if Profile.objects.get(email=email):
            handle_reset_password.delay(email)
            delete_reset_password_token.delay(email)

            return Response(status=status.HTTP_200_OK)

        return Response({'error_message: No DaDay user with this email.'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, email):
        user_id = Profile.objects.get(email=email).user.id
        token_objects = ResetPasswordData.objects.filter(user_id=user_id)
        tokens = [token.token for token in token_objects]

        if self.request.data.get('token') in tokens:
            for token in token_objects:
                token.token_submit = True
            return Response({'user_id': user_id}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)


class NewPasswordView(views.APIView):
    def put(self, request, user_id):
        token_objects = ResetPasswordData.objects.filter(user_id=user_id)

        for token in token_objects:
            if token.token_submit:
                password = self.request.data.get('password')

                profile = UserModel.objects.get(pk=user_id)
                profile.password = make_password(password)
                profile.save()

                return Response(status=status.HTTP_200_OK)

        return Response(
            {'error_message': 'Session expired request another verification email!'},
            status=status.HTTP_404_NOT_FOUND
        )
