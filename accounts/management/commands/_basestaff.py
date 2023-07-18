from django.core.management import BaseCommand, CommandError
from django.core.management.base import CommandParser
from ...models import User


class BasicCommand(BaseCommand):

    def add_arguments(self, parser: CommandParser):
        parser.add_argument("username", metavar="USERNAME", help="Username of User")

    def handle(self, *args, **options):
        try:
            user = User.objects.get(username=options["username"])
        except User.DoesNotExist:
            raise CommandError(f"User with {options['username']} Does not exist!")

        return user
