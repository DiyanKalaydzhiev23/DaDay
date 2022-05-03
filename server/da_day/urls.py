from django.urls import path
from server.common.schedule import start_scheduler
from server.da_day.views import NotesListView, NoteCreateView, NoteDetailsView, SendFriendRequestView, \
    HandleFriendRequestView, \
    SearchForFriendsView, FriendsView, PendingFriendRequestsView

urlpatterns = [
    path('', start_scheduler),
    path('notes/<int:pk>', NotesListView.as_view(), name='notes'),
    path('note/<int:user_id>/<int:pk>', NoteDetailsView.as_view(), name='note details'),
    path('share-day/<int:pk>', NoteCreateView.as_view(), name='share'),
    path('add-friend/<int:user_id>/<int:profile_request_id>', SendFriendRequestView.as_view(), name='send friend request'),
    path('handle-friend-request/<int:user_id>/<int:profile_sending_request_id>', HandleFriendRequestView.as_view(), name='handle request'),
    path('users/<int:user_id>', SearchForFriendsView.as_view(), name='search for friends'),
    path('friends/<int:user_id>/', FriendsView.as_view(), name='friends'),
    path('pending-friend-requests/<int:user_id>/', PendingFriendRequestsView.as_view(), name='pending friend requests'),
]
