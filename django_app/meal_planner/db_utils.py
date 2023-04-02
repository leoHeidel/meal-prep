from datetime import date, timedelta

import yaml


from django.core.exceptions import ValidationError
from .models import Week, Day, Recipe, Ingredient, Instruction


EXAMPLE_RECIPE_DICT =  {
    'name': 'Example Recipe',
    'instructions': [
        'Do this first.',
        'Do this next.',
    ],
    'ingredients': [
        {'name': 'Ingredient 1', 'quantity': '2 cups'},
        {'name': 'Ingredient 2', 'quantity': '1 tsp'},
        {'name': 'Ingredient 3'},
    ],
}


def add_recipe_to_database(recipe_dict):
    """
    Adds a recipe to the database using the given recipe_dict.

    :param recipe_dict: A dictionary containing the recipe information.
        See EXAMPLE_RECIPE_DICT for the format.
    :return: The created Recipe instance, or raises ValidationError if data is invalid.
    """
    if 'name' not in recipe_dict:
        raise ValidationError("Recipe dictionary must contain a 'name' key.")
    if 'ingredients' not in recipe_dict:
        raise ValidationError("Recipe dictionary must contain an 'ingredients' key.")
    if 'instructions' not in recipe_dict:
        raise ValidationError("Recipe dictionary must contain an 'instructions' key.")


    recipe = Recipe.objects.create(name=recipe_dict['name'])

    for ingredient_dict in recipe_dict['ingredients']:
        Ingredient.objects.create(
            name=ingredient_dict['name'],
            quantity=ingredient_dict.get('quantity'),
            recipe=recipe,
        )

    for i, instruction in enumerate(recipe_dict['instructions']):
        Instruction.objects.create(
            step_number=i,
            description=instruction,
            recipe=recipe,
        )
    return recipe

def add_recipe_to_day(recipe_name, day):
    try:
        # Get the recipe object from the database by its name
        recipe = Recipe.objects.filter(name='Pizza').first()

        # Add the recipe to the day's recipes
        day.recipes.add(recipe)
        day.save()

        return True

    except Recipe.DoesNotExist:
        print(f"Recipe '{recipe_name}' does not exist.")
        return False


def string_to_dict(s: str) -> dict:
    try:
        result = ast.literal_eval(s)
        if isinstance(result, dict):
            return result
        else:
            raise ValueError("Input string is not a dictionary")
    except (SyntaxError, ValueError) as e:
        raise ValueError("Invalid input string: {}".format(e))


def get_or_create_current_week_and_days():
    start_of_week = date.today() - timedelta(days=date.today().weekday())
    end_of_week = start_of_week + timedelta(days=6)

    week, created = Week.objects.get_or_create(
        start_date=start_of_week,
        end_date=end_of_week
    )

    if created:
        day_names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        for name in day_names:
            Day.objects.create(name=name, week=week)

    days = Day.objects.filter(week=week)

    return week, days

def display_recipe_names_by_day(week=None):
    """
    Displays all the names of recipe for each day of a week in YAML format.
    """
    if week is None:
        week, _= get_or_create_current_week_and_days()

    days = Day.objects.filter(week=week)
    week_recipe_dict = {}
    for day in days:
        day_recipe_names = []
        for recipe in day.recipes.all():
            day_recipe_names.append(recipe.name)
        week_recipe_dict[day.name] = day_recipe_names

    print(yaml.dump(week_recipe_dict))