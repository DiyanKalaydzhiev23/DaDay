import random
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
        return Response({'question': question}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        text = request.POST.get('text')
        avatar = request.POST.get('avatar')

        note = Note(
            description=text,
            avatar=avatar,
            user=request.user,
        )

        note.save()

        return Response(status=status.HTTP_200_OK)
