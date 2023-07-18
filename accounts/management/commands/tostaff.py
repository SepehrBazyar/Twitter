from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser
from ...models import User


class Command(BaseCommand):

    help = "Command Line Script for Change Staff Users"

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("username", metavar="USERNAME", help="Username of User")

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist:
            raise CommandError(f"User with {options['username']} Does not exist!")

        user.is_staff = True
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Successfully Changed Staff {options['username']} User")
        )
