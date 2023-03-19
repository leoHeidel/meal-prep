from django.core.exceptions import ValidationError
from .models import Recipe, Ingredient, Instruction


EXAMPLE_RECIPE_DICT =  {
    'name': 'Example Recipe',
    'instructions': [
        {'step_number': 1, 'description': 'Do this first.'},
        {'step_number': 2, 'description': 'Do this next.'},
    ],
    'ingredients': [
        {'name': 'Ingredient 1', 'quantity': '2 cups'},
        {'name': 'Ingredient 2', 'quantity': '1 tsp'},
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
            quantity=ingredient_dict['quantity'],
            recipe=recipe,
        )

    for instruction_dict in recipe_dict['instructions']:
        Instruction.objects.create(
            step_number=instruction_dict['step_number'],
            description=instruction_dict['description'],
            recipe=recipe,
        )
    return recipe

def add_recipe_to_day(recipe_name, day):
    try:
        # Get the recipe object from the database by its name
        recipe = Recipe.objects.get(name=recipe_name)

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