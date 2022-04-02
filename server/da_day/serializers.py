from rest_framework import serializers
from server.auth_app.models import Profile
from server.da_day.models import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = ('user',)
