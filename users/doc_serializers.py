from drf_yasg.utils import swagger_serializer_method
from rest_framework import serializers
from users.serializers import UsersDataSerializer


class ResponseUsersList(serializers.Serializer):
    """
    API users list response doc for swagger
    """
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass

    members = serializers.SerializerMethodField(help_text='List of users')

    @swagger_serializer_method(serializer_or_field=UsersDataSerializer(many=True))
    def get_members(self, instance):
        return UsersDataSerializer(many=True)
