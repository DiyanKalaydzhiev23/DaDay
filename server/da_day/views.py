from django.contrib.auth import get_user_model
from rest_framework import views, permissions
from rest_framework.response import Response
from server.da_day.models import Note
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
