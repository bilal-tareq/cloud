from django.core.management.base import BaseCommand
from api.models import Category, Product


class Command(BaseCommand):
    help = 'Seed the database with sample food data'

    def handle(self, *args, **options):
        self.stdout.write('Seeding database...')

        # Clear existing data
        Product.objects.all().delete()
        Category.objects.all().delete()

        # --- Categories ---
        burgers = Category.objects.create(
            name='Burgers',
            description='Juicy handcrafted burgers made with premium ingredients',
            image='https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400',
        )
        pizza = Category.objects.create(
            name='Pizza',
            description='Wood-fired pizzas with fresh toppings',
            image='https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400',
        )
        chicken = Category.objects.create(
            name='Chicken',
            description='Crispy fried and grilled chicken dishes',
            image='https://images.unsplash.com/photo-1626645738196-c2a7c87a8f58?w=400',
        )
        salads = Category.objects.create(
            name='Salads',
            description='Fresh and healthy salad bowls',
            image='https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=400',
        )
        desserts = Category.objects.create(
            name='Desserts',
            description='Sweet treats to end your meal',
            image='https://images.unsplash.com/photo-1551024601-bec78aea704b?w=400',
        )
        drinks = Category.objects.create(
            name='Drinks',
            description='Refreshing beverages and smoothies',
            image='https://images.unsplash.com/photo-1544145945-f90425340c7e?w=400',
        )

        # --- Products ---
        # Burgers
        Product.objects.create(
            category=burgers, name='Classic Smash Burger',
            description='Double smashed patties with American cheese, pickles, and special sauce',
            price=8.99, is_featured=True,
            image='https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=400',
        )
        Product.objects.create(
            category=burgers, name='BBQ Bacon Burger',
            description='Angus beef with crispy bacon, cheddar, and smoky BBQ sauce',
            price=10.99, is_featured=True,
            image='https://images.unsplash.com/photo-1553979459-d2229ba7433b?w=400',
        )
        Product.objects.create(
            category=burgers, name='Mushroom Swiss Burger',
            description='Grilled patty topped with sautéed mushrooms and melted Swiss cheese',
            price=9.99,
            image='https://images.unsplash.com/photo-1572802419224-296b0aeee0d9?w=400',
        )
        Product.objects.create(
            category=burgers, name='Veggie Burger',
            description='Plant-based patty with avocado, tomato, and herb mayo',
            price=8.49,
            image='https://images.unsplash.com/photo-1520072959219-c595dc870360?w=400',
        )

        # Pizza
        Product.objects.create(
            category=pizza, name='Margherita Pizza',
            description='Classic tomato sauce, fresh mozzarella, and basil on a crispy crust',
            price=11.99, is_featured=True,
            image='https://images.unsplash.com/photo-1574071318508-1cdbab80d002?w=400',
        )
        Product.objects.create(
            category=pizza, name='Pepperoni Supreme',
            description='Loaded with pepperoni, mozzarella, and oregano',
            price=13.99,
            image='https://images.unsplash.com/photo-1628840042765-356cda07504e?w=400',
        )
        Product.objects.create(
            category=pizza, name='BBQ Chicken Pizza',
            description='Grilled chicken, red onion, cilantro, and BBQ drizzle',
            price=14.49, is_featured=True,
            image='https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=400',
        )

        # Chicken
        Product.objects.create(
            category=chicken, name='Crispy Chicken Tenders',
            description='Golden fried chicken strips served with honey mustard',
            price=7.99,
            image='https://images.unsplash.com/photo-1562967914-608f82629710?w=400',
        )
        Product.objects.create(
            category=chicken, name='Grilled Chicken Plate',
            description='Herb-marinated grilled chicken with rice and veggies',
            price=11.49, is_featured=True,
            image='https://images.unsplash.com/photo-1632778149955-e80f8ceca2e8?w=400',
        )
        Product.objects.create(
            category=chicken, name='Spicy Wings (8 pcs)',
            description='Buffalo-style wings tossed in our signature hot sauce',
            price=9.49,
            image='https://images.unsplash.com/photo-1567620832903-9fc6debc209f?w=400',
        )

        # Salads
        Product.objects.create(
            category=salads, name='Caesar Salad',
            description='Romaine lettuce, parmesan, croutons, and Caesar dressing',
            price=6.99,
            image='https://images.unsplash.com/photo-1550304943-4f24f54ddde9?w=400',
        )
        Product.objects.create(
            category=salads, name='Greek Salad',
            description='Cucumber, tomato, olives, feta cheese, and olive oil dressing',
            price=7.49, is_featured=True,
            image='https://images.unsplash.com/photo-1540420773420-3366772f4999?w=400',
        )

        # Desserts
        Product.objects.create(
            category=desserts, name='Chocolate Lava Cake',
            description='Warm chocolate cake with a molten center, served with vanilla ice cream',
            price=6.99, is_featured=True,
            image='https://images.unsplash.com/photo-1624353365286-3f8d62daad51?w=400',
        )
        Product.objects.create(
            category=desserts, name='New York Cheesecake',
            description='Creamy classic cheesecake with strawberry topping',
            price=5.99,
            image='https://images.unsplash.com/photo-1567171466295-4afa63d45416?w=400',
        )
        Product.objects.create(
            category=desserts, name='Tiramisu',
            description='Italian coffee-flavored layered dessert with mascarpone',
            price=6.49,
            image='https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=400',
        )

        # Drinks
        Product.objects.create(
            category=drinks, name='Fresh Mango Smoothie',
            description='Blended mango with yogurt and a touch of honey',
            price=4.99,
            image='https://images.unsplash.com/photo-1546173159-315724a31696?w=400',
        )
        Product.objects.create(
            category=drinks, name='Iced Caramel Latte',
            description='Espresso with caramel syrup and cold milk over ice',
            price=4.49,
            image='https://images.unsplash.com/photo-1461023058943-07fcbe16d735?w=400',
        )
        Product.objects.create(
            category=drinks, name='Fresh Lemonade',
            description='Freshly squeezed lemonade with mint leaves',
            price=3.49,
            image='https://images.unsplash.com/photo-1621263764928-df1444c5e859?w=400',
        )

        total = Product.objects.count()
        cats = Category.objects.count()
        self.stdout.write(self.style.SUCCESS(
            f'Successfully seeded {cats} categories and {total} products!'
        ))
