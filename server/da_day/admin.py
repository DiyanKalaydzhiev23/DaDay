from django.contrib import admin
from server.da_day.models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass

