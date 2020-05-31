from rest_framework import serializers
from helper import keys, model_keys
from users.models import UsersActivityPeriodsData, UsersData


class UserActivityPeriodSerializer(serializers.ModelSerializer):
    """
    Serializer for getting user's activity periods
    """
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    def get_start_time(self, instance):
        """
        Get activity period start time in local timezone
        :param instance:
        :return:
        """
        return instance.local_start_time.strftime(keys.START_TIME_FORMAT)

    def get_end_time(self, instance):
        """
        Get activity period end time in local timezone
        :param instance:
        :return:
        """
        return instance.local_end_time.strftime(keys.END_TIME_FORMAT)

    class Meta:
        model = UsersActivityPeriodsData
        fields = [model_keys.START_TIME, model_keys.END_TIME]


class UsersDataSerializer(serializers.ModelSerializer):
    """
    Serializer for getting user's data with all activity periods
    """
    real_name = serializers.CharField(source='name')
    activity_periods = serializers.SerializerMethodField(help_text="List of activity periods")

    def get_activity_periods(self, instance):
        """
        Get serializer data of user's activity periods
        :param instance:
        :return:
        """
        return UserActivityPeriodSerializer(instance.usersactivityperiodsdata_set.order_by('start_time', 'end_time'),
                                            many=True).data

    class Meta:
        model = UsersData
        fields = [model_keys.ID, model_keys.REAL_NAME, model_keys.TZ, model_keys.ACTIVITY_PERIODS]
