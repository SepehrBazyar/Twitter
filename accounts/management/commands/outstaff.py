from ._basestaff import BasicCommand


class Command(BasicCommand):

    help = "Command Line Script for Change Staff Users for Non Staff"

    def handle(self, *args, **options):
        user = super().handle(*args, **options)
        user.is_staff = False
        user.save()
        self.stdout.write(
            self.style.WARNING(f"Successfully Changed Staff {options['username']} User")
        )
