from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import permissions, generics, status, views
from rest_framework.response import Response
from server.auth_app.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings


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
        self.my_mail(request, request.data.get('profile.parent_email'))
        return Response({'token': token.key}, status=status.HTTP_201_CREATED, headers=headers)

    @staticmethod
    def my_mail(request=None, email=None):

        if request:
            subject = "Registration greetings"
        else:
            subject = "else"

        msg = "We are pleasured to see that you choose DaDay for personal diary for your child. " \
              "We can ensure you that we will deliver the best possible experience for your beloved one " \
              "and give you monthly reports on their mental health status. " \
              "" \
              "Regards," \
              "AllowCookiesTeam"

        to = email
        res = send_mail(subject, msg, settings.EMAIL_HOST_USER, [to])

        if res == 1:
            msg = "Mail Sent Successfully."
        else:
            msg = "Mail Sending Failed."

        return HttpResponse(msg)


class LoginUserView(views.APIView):
    queryset = UserModel.objects.all()
    permission_classes = (permissions.AllowAny,)

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

            data = {
                'token': token.key,
                'user_id': request.user.pk,
                'username': request.user.username
            }

            return Response(data, status=status.HTTP_201_CREATED)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
