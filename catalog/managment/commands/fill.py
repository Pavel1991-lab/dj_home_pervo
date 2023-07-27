import os

from django.core.management import BaseCommand

from catalog.models import Category
# from config import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# settings.configure()

class Command(BaseCommand):

    def handle(self, *args, **options):
        category = [
            {'name': 'Ягода', 'description': 'Вкусная'}
        ]

        cetegory_create = []
        for i in category:
            cetegory_create.append(
                Category(**i)
            )

        Category.objects.bulk_create(cetegory_create)