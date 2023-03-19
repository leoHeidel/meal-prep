import json

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from meal_planner.models import Week, Day, Recipe, Ingredient, Instruction
from django.views.decorators.csrf import ensure_csrf_cookie
from django.core import serializers

@ensure_csrf_cookie
def dashboard(request):
    # Get the most recent week
    week = Week.objects.latest('start_date')

    # Get the days for the week and their associated recipes
    days = Day.objects.filter(week=week).prefetch_related('recipes')

    # Render the data to the dashboard template
    return render(request, 'dashboard.html', {'week': week, 'days': days})

def recipe_detail(request, recipe_id):
    # Get the recipe object from the database
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Render the data to the recipe_detail template
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def recipe_detail_json(request, recipe_id):
    # Get the recipe object from the database
    recipe = get_object_or_404(Recipe, id=recipe_id)

    # Get the ingredients for the recipe
    ingredients = Ingredient.objects.filter(recipe=recipe)

    # Get the instructions for the recipe
    instructions = Instruction.objects.filter(recipe=recipe)

    # Create a dictionary with the recipe data
    recipe_data = {
        'name': recipe.name,
        'ingredients': [
            {
                'name': ingredient.name,
                'quantity': ingredient.quantity
            } for ingredient in ingredients
        ],
        'instructions': [
            {
                'step_number': instruction.step_number,
                'description': instruction.description
            } for instruction in instructions
        ]
    }

    # Return the recipe data as JSON
    return JsonResponse(recipe_data)


def generate_recipe_for_day(request, day_id):
    # Extract the user_message from the request body
    data = json.loads(request.body)
    user_message = data.get('user_message', '')

    # Your logic for generating a recipe based on the user_message and adding it to the day
    # ... (your logic here)

    new_recipe = get_object_or_404(Recipe, id=2)
    # Serialize the new recipe to JSON
    new_recipe_json = serializers.serialize('json', [new_recipe])

    # Return a JsonResponse containing the new recipe data
    return JsonResponse({'result': 'success', 'new_recipe': new_recipe_json})