from django.core.management.base import BaseCommand
from django.contrib.auth.models import User, Permission

class Command(BaseCommand):
    help = 'Create demo user'

    def handle(self, *args, **kwargs):
        user, created = User.objects.get_or_create(username="demo")

        if created:
            user.set_password("demo123")
            user.is_staff = True
            user.is_superuser = False
            user.save()

            permissions = Permission.objects.filter(codename__startswith="view_")
            user.user_permissions.set(permissions)

            self.stdout.write(self.style.SUCCESS("Demo user created"))
        else:
            self.stdout.write("Demo user already exists")
