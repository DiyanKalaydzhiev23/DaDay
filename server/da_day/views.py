from rest_framework import views
from rest_framework.response import Response

from server.da_day.models import Note
from server.da_day.serializers import NoteSerializer


class NotesListView(views.APIView):
    def get(self, request, pk):
        notes = Note.objects.filter(user=pk)
        serializer = NoteSerializer(notes, many=True)

        return Response(data=serializer.data)
