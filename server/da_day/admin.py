from django.contrib import admin
from server.da_day.models import Note, Question


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    pass
