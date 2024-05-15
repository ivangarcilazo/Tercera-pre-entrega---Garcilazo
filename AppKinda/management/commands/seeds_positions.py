from django.core.management.base import BaseCommand
from AppKinda.models import Position

class Command(BaseCommand):
    help = 'Seed positions into the database'

    def handle(self, *args, **kwargs):
        positions = ['Gerente general', 'Gerente de ventas', 'Vendedor de autos', 'Asesor de financiamiento']

        for position_name in positions:
            position, created = Position.objects.get_or_create(name=position_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Position "{position_name}" created successfully'))
            else:
                self.stdout.write(self.style.WARNING(f'Position "{position_name}" already exists'))