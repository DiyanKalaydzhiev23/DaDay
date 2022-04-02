from django.urls import path

from server.common.schedule import start_scheduler
from server.da_day.views import NotesListView, NoteCreateView

urlpatterns = [
    path('', start_scheduler),
    path('notes/<int:pk>', NotesListView.as_view(), name='note'),
    path('share-day/<int:pk>', NoteCreateView.as_view(), name='share'),
]
