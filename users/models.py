import random
import string
from django.db import models
import pytz


class UsersData(models.Model):
    """
    User (Member) table
    """
    # Get list of all the timezones
    TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

    # Primary field
    id = models.CharField(max_length=255, primary_key=True, unique=True, editable=False)
    # Name of the user
    name = models.CharField(max_length=255)
    # timezone from where the user belongs to
    tz = models.CharField(max_length=50, choices=TIMEZONES, default='UTC')

    # Save created and modified datetime of instance automatically when changes
    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.id

    def save(self, *args, **kwargs):
        """
        Overriding model save method to generate unique primary id for the new instance
        :param args:
        :param kwargs:
        :return:
        """

        def get_random_alpha_numeric_string(string_length=7):
            """
            Getting random alpha numeric string of defined string length
            Given fixed prefix 'WO'
            :param string_length:
            :return:
            """
            letters_and_digits = string.ascii_uppercase + string.digits
            return 'W0' + ''.join((random.choice(letters_and_digits) for i in range(string_length)))

        # Generating random id for the new instance
        while not self.id:
            new_id = get_random_alpha_numeric_string()

            # Check the new id if its already being used by other instance
            if not UsersData.objects.filter(id=new_id).exists():
                self.id = new_id

        super().save(*args, **kwargs)


class UsersActivityPeriodsData(models.Model):
    """
    Table for saving user activities
    """
    user = models.ForeignKey(UsersData, on_delete=models.CASCADE)

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    created = models.DateTimeField(auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(auto_now=True, auto_now_add=False)

    @property
    def local_start_time(self):
        """
        Property to get activity period 'local start time' by the user timezone
        :return: datetime object
        """
        utc = self.start_time.replace(tzinfo=pytz.UTC)
        local_tz = utc.astimezone(pytz.timezone(self.user.tz))
        return local_tz

    @property
    def local_end_time(self):
        """
        Property to get activity period 'local end time' by the user timezone
        :return: datetime object
        """
        utc = self.end_time.replace(tzinfo=pytz.UTC)
        local_tz = utc.astimezone(pytz.timezone(self.user.tz))
        return local_tz

    def __str__(self):
        return str(self.id)
