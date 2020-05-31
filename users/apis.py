from django.core import management
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from helper import keys
from users import doc_serializers
from users.models import UsersData
from users.serializers import UsersDataSerializer


@swagger_auto_schema(
    operation_id='Users List', operation_description="Get all the users with their all activity periods", method='GET',
    responses={
        200: doc_serializers.ResponseUsersList
    }
)
@api_view(['GET'])
def api_users_list(request):
    """
    API to get all the user's list with their activity period details
    :param request:
    :return:
    """
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


@swagger_auto_schema(
    operation_id='Reset Users List', operation_description="Reset all the users data and fill DB with mock data",
    method='GET'
)
@api_view(['GET'])
def api_reset_users(request):
    """
    API to call management command to reset users data
    :param request:
    :return:
    """
    management.call_command('reset-users-data')
    return Response({keys.OK: True}, status=status.HTTP_200_OK)
