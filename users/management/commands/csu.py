from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.com',
            first_name='Admin',
            last_name='Dz_py'
        )

        user.set_password('200818')
        user.save()
