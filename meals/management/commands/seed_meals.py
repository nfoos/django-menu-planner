import random

from django.core.management.base import BaseCommand

from meals.models import Menu, Meal, MealItem
from meals.dates import previous_week, end_of_week, next_day


class Command(BaseCommand):
    help = 'Inserts test data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--menu',
            default='Sigma Kappa',
            help='Name of the menu to seed',
        )

    def handle(self, *args, **options):
        menu, created = Menu.objects.get_or_create(name=options['menu'])

        date = previous_week()
        end_date = end_of_week()

        while date <= end_date:
            add_meal(menu, date, "lunch")
            add_meal(menu, date, "dinner")

            date = next_day(date)


def add_meal(menu, date, type):
    meal, created = Meal.objects.get_or_create(menu=menu, date=date, type=type)

    if created:
        add_entre(meal)
        add_side(meal)
        add_side(meal)


def add_entre(meal):
    name = random.choice(dishes())
    add_meal_item(meal, 'entre', name)


def add_side(meal):
    name = random.choice(vegetables() + fruits())
    add_meal_item(meal, 'side', name)


def add_meal_item(meal, type, name):
    MealItem.objects.create(
        meal=meal,
        type=type,
        name=name,
        is_dairy_free=random.choice([True, False]),
        is_gluten_free=random.choice([True, False]),
        is_vegetarian=random.choice([True, False]),
    )


def dishes():
    return["Arepas", "Barbecue Ribs", "Bruschette with Tomato", "Bunny Chow", "Caesar Salad", "California Maki", "Caprese Salad", "Cauliflower Penne", "Cheeseburger", "Chicken Fajitas", "Chicken Milanese", "Chicken Parm", "Chicken Wings", "Chilli con Carne", "Ebiten maki", "Fettuccine Alfredo", "Fish and Chips", "French Fries with Sausages", "French Toast", "Hummus", "Katsu Curry", "Kebab", "Lasagne", "Linguine with Clams", "Massaman Curry", "Meatballs with Sauce", "Mushroom Risotto", "Pappardelle alla Bolognese", "Pasta Carbonara", "Pasta and Beans", "Pasta with Tomato and Basil", "Peking Duck", "Philadelphia Maki", "Pho", "Pierogi", "Pizza", "Poke", "Pork Belly Buns", "Pork Sausage Roll", "Poutine", "Ricotta Stuffed Ravioli", "Risotto with Seafood", "Salmon Nigiri", "Scotch Eggs", "Seafood Paella", "Som Tam", "Souvlaki", "Stinky Tofu", "Sushi", "Tacos", "Teriyaki Chicken Donburi", "Tiramisù", "Tuna Sashimi", "Vegetable Soup"]


def fruits():
    return ["Apples", "Apricots", "Aubergine", "Avocado", "Banana", "Berries", "Blackberries", "Blood oranges", "Blueberries", "Bush Tomato", "Butternut pumpkin", "Cantaloupe", "Cavalo", "Starfruit", "Cherries", "Corella Pear", "Cranberry", "Cumquat", "Currants", "Custard Apples", "Custard Apples Daikon", "Dates", "Dragonfruit", "Dried Apricots", "Elderberry", "Feijoa", "Grapefruit", "Grapes", "Figs", "Fingerlime", "Goji Berry", "Guava", "Honeydew melon", "Incaberries", "Jarrahdale pumpkin", "Juniper Berries", "Kiwi Fruit", "Kiwiberries", "Lemon", "Limes", "Longan", "Loquats", "Lychees", "Mango", "Mangosteens", "Melon", "Mandarins", "Mulberries", "Nashi Pear", "Nectarines", "Olives", "Oranges", "Papaw", "Papaya", "Passionfruit", "Peaches", "Pears", "Pineapple", "Pomegranate", "Plums", "Prunes", "Rockmelon", "Snowpeas", "Sprouts", "Strawberries", "Sultanas", "Tangelo", "Tomatoes", "Watermelon"]


def vegetables():
    return ["Artichoke", "Arugula", "Asian Greens", "Asparagus", "Bean Shoots", "Bean Sprouts", "Beans", "Green beans", "Beetroot", "Bok Choy", "Broccoli", "Broccolini", "Brussels Sprouts", "Butternut lettuce", "Cabbage", "Capers", "Carob Carrot", "Carrot", "Cauliflower", "Celery", "Chilli Pepper", "Chinese Cabbage", "Fresh Chillies", "Dried Chinese Broccoli", "Cornichons", "Cos lettuce", "Cucumber", "Eggplant", "Endive", "English Spinach", "French eschallots", "Garlic", "Chives", "Green Pepper", "Hijiki", "Iceberg lettuce", "Jerusalem Artichoke", "Jicama", "Kale", "Kohlrabi", "Leeks", "Lettuce", "Onion", "Okra", "Parsnip", "Peas", "Peppers", "Potatoes", "Pumpkin", "Purple carrot", "Radicchio", "Radish", "Raspberry", "Red cabbage", "Red Pepper", "Rhubarb", "Snowpea sprouts", "Spinach", "Squash", "Sun dried tomatoes", "Sweet Potato", "Swiss Chard", "Turnips", "Zucchini"]
