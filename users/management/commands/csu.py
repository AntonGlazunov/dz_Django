from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='admins@mail.com',
            first_name='Admin',
            last_name='Dz_py',
            is_staff=True,
            is_superuser=True
        )

        user.set_password('200818')
        user.save()