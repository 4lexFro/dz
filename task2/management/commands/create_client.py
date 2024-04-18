from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from task2.models import Client
# запуск командой python manage.py create_client

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='Tom', email='tom@example.com', phone_number ='89274563490', address='Omsk.Gluhaya,34', registration_date=datetime.strftime(timezone.now(), '%Y-%m-%d %H:%M'))
        client.save()
        self.stdout.write(f'{client}')