from datetime import datetime

from django.core.management.base import BaseCommand
from django.utils import timezone

from task2.models import Product

class Command(BaseCommand):
    help = "Create product."

    def handle(self, *args, **kwargs):
        product = Product(name='Кефир', description='Очень полезный продукт', price ='83.23', quantity='10', added_date=datetime.strftime(timezone.now(), '%Y-%m-%d %H:%M'))
        product.save()
        self.stdout.write(f'{product}')