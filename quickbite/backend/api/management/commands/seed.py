import os
import requests
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from api.models import Category, Product


class Command(BaseCommand):
    help = 'Seed the database with sample food data and upload images to S3'

    def download_image(self, url, name):
        """Helper to download image and return a ContentFile."""
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return ContentFile(response.content, name=f"{name}.jpg")
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Failed to download {url}: {e}'))
        return None

    def handle(self, *args, **options):
        self.stdout.write('Seeding database and uploading images to S3...')

        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # --- Categories ---
        categories_data = [
            ('Burgers', 'Juicy handcrafted burgers made with premium ingredients', 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600'),
            ('Pizza', 'Wood-fired pizzas with fresh toppings', 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600'),
            ('Chicken', 'Crispy fried and grilled chicken dishes', 'https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?w=600'),
            ('Salads', 'Fresh and healthy salad bowls', 'https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600'),
            ('Desserts', 'Sweet treats to end your meal', 'https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600'),
            ('Drinks', 'Refreshing beverages and smoothies', 'https://images.unsplash.com/photo-1544145945-f90425340c7e?w=600'),
        ]

        cats = {}
        for name, desc, url in categories_data:
            cat = Category.objects.create(name=name, description=desc)
            img_file = self.download_image(url, name.lower())
            if img_file:
                cat.image.save(f"{name.lower()}.jpg", img_file, save=True)
            cats[name] = cat
            self.stdout.write(f'Created category: {name}')

        # --- Products ---
        products_data = [
            # Burgers
            (cats['Burgers'], 'Classic Smash Burger', 'Double smashed patties with American cheese, pickles, and special sauce', 8.99, True, 'https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600'),
            (cats['Burgers'], 'BBQ Bacon Burger', 'Angus beef with crispy bacon, cheddar, and smoky BBQ sauce', 10.99, True, 'https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=600'),
            (cats['Burgers'], 'Mushroom Swiss Burger', 'Grilled patty topped with sautéed mushrooms and melted Swiss cheese', 9.99, False, 'https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=600'),
            
            # Pizza
            (cats['Pizza'], 'Margherita Pizza', 'Classic tomato sauce, fresh mozzarella, and basil on a crispy crust', 11.99, True, 'https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=600'),
            (cats['Pizza'], 'BBQ Chicken Pizza', 'Grilled chicken, red onion, cilantro, and BBQ drizzle', 14.49, True, 'https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600'),
            
            # Chicken
            (cats['Chicken'], 'Grilled Chicken Plate', 'Herb-marinated grilled chicken with rice and veggies', 11.49, True, 'https://images.unsplash.com/photo-1632778149955-e80f8ceca2e8?w=600'),
            
            # Salads
            (cats['Salads'], 'Greek Salad', 'Cucumber, tomato, olives, feta cheese, and olive oil dressing', 7.49, True, 'https://images.unsplash.com/photo-1540420773420-3366772f4999?w=600'),
            
            # Desserts
            (cats['Desserts'], 'Chocolate Lava Cake', 'Warm chocolate cake with a molten center, served with vanilla ice cream', 6.99, True, 'https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=600'),
            
            # Drinks
            (cats['Drinks'], 'Fresh Mango Smoothie', 'Blended mango with yogurt and a touch of honey', 4.99, False, 'https://images.unsplash.com/photo-1546173159-315724a31696?w=600'),
        ]

        for cat, name, desc, price, featured, url in products_data:
            prod = Product.objects.create(
                category=cat, name=name, description=desc, 
                price=price, is_featured=featured
            )
            img_file = self.download_image(url, name.replace(' ', '_').lower())
            if img_file:
                prod.image.save(f"{name.replace(' ', '_').lower()}.jpg", img_file, save=True)
            self.stdout.write(f'Created product: {name}')

        total = Product.objects.count()
        cat_count = Category.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully seeded {cat_count} categories and {total} products with images uploaded to S3!'
        ))
