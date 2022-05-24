import random
from django.contrib.auth import get_user_model
from rest_framework import views, status
from rest_framework.response import Response

from server.auth_app.models import Profile
from server.auth_app.serializers import ProfileSerializer
from server.chats_app.models import Room
from server.common.helpers import authenticated_user
from server.da_day.models import Note, Question
from server.da_day.serializers import NoteSerializer


UserModel = get_user_model()


class NotesListView(views.APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, pk):
        authenticated_user(request, pk)

        if self.request.query_params.get('sorting') == 'asc':
            queryset = Note.objects.filter(user=pk).order_by('date')
        else:
            queryset = Note.objects.filter(user=pk).order_by('-date')

        serializer = NoteSerializer(queryset, many=True)

        return Response(data=serializer.data)


class NoteDetailsView(views.APIView):
    def get(self, request, user_id, pk):
        authenticated_user(request, user_id)
        queryset = Note.objects.get(pk=pk)
        serializer = NoteSerializer(queryset, many=False)

        return Response({'note': serializer.data}, status=status.HTTP_200_OK)


class NoteCreateView(views.APIView):
    queryset = Question.objects.all()

    def get(self, request, pk):
        authenticated_user(request, pk)
        question = random.choice(self.queryset.all()).__str__()

        return Response({'question': question}, status=status.HTTP_200_OK)

    def post(self, request, pk):
        text = request.data.get('text')
        avatar = request.data.get('avatar')

        user = UserModel.objects.get(id=pk)

        note = Note(
            description=text,
            emotion=avatar,
            user=user,
        )

        note.save()

        all_notes = Note.objects.filter(user_id=pk)

        if len(all_notes) >= 60:
            first_note = list(all_notes).pop(0)
            first_note.delete()

        return Response(status=status.HTTP_200_OK)


class SendFriendRequestView(views.APIView):
    def get(self, request, user_id, profile_request_id):
        authenticated_user(request, user_id)

        profile_request = Profile.objects.get(pk=profile_request_id)
        already_sent_request = False

        serializer = ProfileSerializer(profile_request, many=False)

        if user_id in profile_request.pending_friend_requests:
            already_sent_request = True

        return Response({
            'already_sent_request': already_sent_request,
            'profile': serializer.data,
        }, status=status.HTTP_200_OK)

    def post(self, request, user_id, profile_request_id):
        authenticated_user(request, user_id)

        profile_request = Profile.objects.get(pk=profile_request_id)
        profile_request.pending_friend_requests.append(user_id)
        profile_request.save()

        return Response(status=status.HTTP_200_OK)


class HandleFriendRequestView(views.APIView):
    def post(self, request, user_id, profile_sending_request_id):
        authenticated_user(request, user_id)

        profile = Profile.objects.get(pk=user_id)
        profile_sending_request = Profile.objects.get(pk=profile_sending_request_id)

        user = UserModel.objects.get(pk=user_id)
        user_sending_request = UserModel.objects.get(pk=profile_sending_request_id)

        if self.request.query_params.get('accept_request'):
            if len(profile.friends) < 5000:
                profile.pending_friend_requests.remove(profile_sending_request_id)
                profile.friends.append(profile_sending_request_id)
                profile_sending_request.friends.append(user_id)

                room = Room()
                room.room_name = user.username + 'AND' + user_sending_request.username
                room.save()
            else:
                return Response(status=status.HTTP_417_EXPECTATION_FAILED)

        elif self.request.query_params.get('remove_request'):
            profile.pending_friend_requests.remove(profile_sending_request_id)

        elif self.request.query_params.get('remove_friend'):
            profile.friends.remove(profile_sending_request_id)
            profile_sending_request.friends.remove(user_id)

            room = Room.objects.get(room_name=user.username + 'AND' + user_sending_request.username)
            room.delete()

        profile.save()

        return Response(status=status.HTTP_200_OK)


class SearchForFriendsView(views.APIView):
    def get(self, request, user_id):
        authenticated_user(request, user_id)
        searched_username = self.request.query_params.get('username')

        if searched_username:
            users = UserModel.objects.get(username__icontains=searched_username)
        else:
            all_users = UserModel.objects.all()
            users_to_show = 100

            if len(all_users) < 100:
                users_to_show = len(all_users) - 2

            users = random.sample((list(all_users)), users_to_show)

        users = [
            {
                'profile': ProfileSerializer(Profile.objects.get(pk=user.id)).data,
                'id': user.id
            }
            for user in users if user_id != user.id
        ]

        return Response({"users": users}, status=status.HTTP_200_OK)


class FriendsView(views.APIView):
    def get(self, request, user_id):
        authenticated_user(request, user_id)

        profile = Profile.objects.get(pk=user_id)
        friends = [
            {
                'profile': ProfileSerializer(Profile.objects.get(pk=friend_id)).data,
                'id': friend_id,
            }

            for friend_id in profile.friends
        ]

        return Response({'friends': friends}, status=status.HTTP_200_OK)


class PendingFriendRequestsView(views.APIView):
    def get(self, request, user_id):
        authenticated_user(request, user_id)

        profile = Profile.objects.get(pk=user_id)
        pending_friend_requests = [
            {
                'profile': ProfileSerializer(Profile.objects.get(pk=user_id)).data,
                'id': user_id,
            }

            for user_id in profile.pending_friend_requests
        ]

        return Response({'pending_friend_requests': pending_friend_requests}, status=status.HTTP_200_OK)
