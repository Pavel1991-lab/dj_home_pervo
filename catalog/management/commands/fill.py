import os

from django.core.management import BaseCommand

from catalog.models import Product, Category
# from config import settings

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
# settings.configure()

class Command(BaseCommand):

    def handle(self, *args, **options):
        product = [
            {'name': 'Картошка', 'description': 'У нас вкусная картоошка по доступным ценам, оптом, от 100 кг скидка 25%',
             'image': 'product_images/картошка.jpg', 'category': Category.objects.get(id=2), 'purchase_price': 30 },
            {'name': 'Малина',
             'description': 'Вкуснейшая ягода, полезная для зрения, по очень хорошей цене, всего 200 рублей за кг., при покупке от 10 кг. Меньше 10 кг не продаем, едим сами.',
             'image': 'product_images/малиа.jpeg', 'category': Category.objects.get(id=3), 'purchase_price': 200},
            {'name': 'Яблоки',
             'description': 'У нас вкусные и полезные яблоки с местных садов. При покупке оптом от 50 кг скидка 20%',
             'image': 'product_images/яблоки.jpg', 'category': Category.objects.get(id=1), 'purchase_price': 100},
            {'name': 'Груши',
             'description': 'Спелые, сочные груши только в нашем магазине. При покупке оптом от 100 кг скидка 10%',
             'image': 'product_images/гр.jpg', 'category': Category.objects.get(id=1), 'purchase_price': 150}
        ]



        cetegory_create = []
        for i in product:
            cetegory_create.append(
                Product(**i)
            )

        Product.objects.bulk_create(cetegory_create)