import random
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from rest_framework import views, permissions, status
from rest_framework.response import Response
from server.da_day.models import Note, Question
from server.da_day.serializers import NoteSerializer


UserModel = get_user_model()


class NotesListView(views.APIView):
    def get(self, request, pk):
        queryset = Note.objects.filter(user=pk)
        serializer = NoteSerializer(queryset, many=True)
        permission_classes = (
            permissions.AllowAny,
        )

        return Response(data=serializer.data)


class NoteCreateView(views.APIView):
    queryset = Question.objects.all()
    permission_classes = (
        permissions.AllowAny,
    )

    def get(self, request, pk):
        question = random.choice(self.queryset.all()).__str__()

        if request.headers.get('Authorization') in Token.objects.get_or_create(user=request.user.id):
            return Response({'question': question}, status=status.HTTP_200_OK)

        return Response(status=status.HTTP_404_NOT_FOUND)
