from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

import keys
from users.models import UsersData
from users.serializers import UsersDataSerializer


@api_view(['GET'])
def api_users_list(request):
    try:
        users_serializer = UsersDataSerializer(UsersData.objects.all(), many=True)
        return Response({
            keys.OK: True,
            keys.MEMBERS: users_serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            keys.OK: False,
            keys.ERROR: str(e)
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
