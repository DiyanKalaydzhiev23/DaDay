from rest_framework import views, status
from server.chats_app.models import TextMessage, Room
from rest_framework.response import Response
from server.common.helpers import authenticated_user


class ChatView(views.APIView):
    def get(self, request, room_name):
        authenticated_user(request, request.data.get('user_id'))

        room_id = Room.objects.get(room_name=room_name).id

        return Response(data={
            'messages': TextMessage.objects.filter(id=room_id),
        }, status=status.HTTP_200_OK)
