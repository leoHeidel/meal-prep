
from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from meal_planner.models import Week, Day, Recipe, Ingredient

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

    # Create a dictionary with the recipe data
    recipe_data = {
        'name': recipe.name,
        'instructions': recipe.instructions,
        'ingredients': [
            {
                'name': ingredient.name,
                'quantity': ingredient.quantity
            } for ingredient in ingredients
        ]
    }

    # Return the recipe data as JSON
    return JsonResponse(recipe_data)