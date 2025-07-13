from django.core.management.base import BaseCommand
from properties.models import Property
from decimal import Decimal

class Command(BaseCommand):
    help = 'Create demo property data'

    def handle(self, *args, **options):
        # Clear existing data
        Property.objects.all().delete()
        
        # Create demo properties
        properties = [
            {
                'title': 'Modern Downtown Apartment',
                'description': 'Beautiful 2-bedroom apartment in the heart of downtown with amazing city views.',
                'price': Decimal('2500.00'),
                'location': 'Downtown'
            },
            {
                'title': 'Cozy Suburban House',
                'description': 'Charming 3-bedroom house with a large backyard, perfect for families.',
                'price': Decimal('3200.00'),
                'location': 'Suburbia'
            },
            {
                'title': 'Luxury Penthouse',
                'description': 'Stunning penthouse with panoramic views and premium amenities.',
                'price': Decimal('8500.00'),
                'location': 'Uptown'
            },
            {
                'title': 'Beach House',
                'description': 'Relaxing beachfront property with direct ocean access.',
                'price': Decimal('4500.00'),
                'location': 'Beachfront'
            },
            {
                'title': 'Mountain Cabin',
                'description': 'Rustic cabin nestled in the mountains, perfect for weekend getaways.',
                'price': Decimal('1800.00'),
                'location': 'Mountains'
            }
        ]
        
        for prop_data in properties:
            property = Property.objects.create(**prop_data)
            self.stdout.write(
                self.style.SUCCESS(f'Created property: {property.title}')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {len(properties)} demo properties')
        )