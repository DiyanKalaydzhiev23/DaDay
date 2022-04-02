from django.urls import path

from server.da_day.views import NotesListView

urlpatterns = [
    path('notes/<int:pk>', NotesListView.as_view(), name='note'),
]
