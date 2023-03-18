from django.db import models


class Ingredient(models.Model):
    """
    Model to hold an ingredient for a recipe.
    """
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.quantity} {self.name}"


class Recipe(models.Model):
    """
    Model to hold a recipe, along with its ingredients and instructions.
    """
    name = models.CharField(max_length=100)
    instructions = models.TextField()

    def __str__(self):
        return self.name
    
    
class Week(models.Model):
    """
    Model to hold a week of meal planning.
    """
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Week {self.pk}: {self.start_date} - {self.end_date}"

class Day(models.Model):
    """
    Model to hold a day of meal planning.
    """
    name = models.CharField(max_length=100)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return f"{self.name} ({self.week})"
