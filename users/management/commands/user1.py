from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email='user@mail.com',
            first_name='Пользователь',
            last_name='Пользователев',
        )

        user.set_password('200818')
        user.save()
