from django.urls import path
from meal_planner import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('recipe/<int:recipe_id>/', views.recipe_detail, name='recipe_detail'),
    path('recipe/<int:recipe_id>/json/', views.recipe_detail_json, name='recipe_detail_json'),
    path('day/<int:day_id>/generate_recipe/', views.generate_recipe_for_day, name='generate_recipe_for_day'),
]
