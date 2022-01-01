from django.core.management.base import BaseCommand
from authapp.models import User, UserProfile


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = User.objects.all()
        for user in users:
            UserProfile.objects.create(user=user)