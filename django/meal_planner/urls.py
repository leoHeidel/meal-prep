from django.urls import path
from meal_planner.views import dashboard, recipe_detail, recipe_detail_json

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('recipe/<int:recipe_id>/', recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/json/', recipe_detail_json, name='recipe_detail_json'),
]
