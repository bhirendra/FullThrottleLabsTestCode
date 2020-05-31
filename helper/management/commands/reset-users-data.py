import random
import pytz
from django.core.management import BaseCommand
from mixer.auto import mixer
from users.models import UsersData, UsersActivityPeriodsData
from faker import Faker

fake = Faker()


class Command(BaseCommand):
    help = 'Management command to reset users data and add mock data'

    def handle(self, *args, **options):
        """ Remove existing data """
        UsersData.objects.all().delete()
        self.stdout.write(self.style.SUCCESS("All the existing users cleared"))

        """ Generate mock data """
        timezones = pytz.all_timezones

        mock_user_count = 10

        for i in range(0, mock_user_count):
            user = UsersData.objects.create(
                name=fake.name(),
                tz=random.choice(timezones)
            )

            mock_activity_factors_count = random.randint(1, 5)

            for j in range(0, mock_activity_factors_count):
                _ = mixer.blend(UsersActivityPeriodsData, user=user)

        self.stdout.write(self.style.SUCCESS("Added "+str(mock_user_count)+"new users with their activity periods of "
                                                                           "total 1-5 (Random)"))
