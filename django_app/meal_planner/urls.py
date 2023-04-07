from django.urls import path
from meal_planner import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
