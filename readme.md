## Project architecture

meal-prep/
    ├── gpt_utils/
    │   └── describe_dir.py        # utility script to print a directory tree structure
    ├── recipes-examples.md        # file with some recipe examples for testing
    ├── start_server.sh            # shell script to activate conda environment and start Django server
    ├── readme.md                  # README file with instructions and information about the project
    └── django/                    # directory for Django web application
        ├── db.sqlite3             # SQLite database file for Django project
        ├── PrepPilot/             # directory for Django project (unused in this project)
        │   ├── asgi.py            # ASGI configuration file
        │   ├── __init__.py        # empty init file to indicate a package
        │   ├── settings.py        # project-level settings file
        │   ├── urls.py            # project-level URL configuration file
        │   └── wsgi.py            # WSGI configuration file
        ├── meal_planner/           # directory for meal planning app
        │   ├── migrations/        # directory for Django database migrations
        │   │   ├── 0001_initial.py           # migration for creating the Week, Day, Recipe, and Ingredient models
        │   │   ├── 0002_day_recipes.py        # migration for adding the ManyToManyField for recipes in Day model
        │   │   └── __init__.py
        │   ├── models.py           # file defining the Week, Day, Recipe, and Ingredient models
        │   ├── __init__.py         # empty init file to indicate a package
        │   ├── apps.py             # file defining the MealPlannerConfig app configuration class
        │   ├── admin.py            # file defining the admin interface for the Week, Day, Recipe, and Ingredient models
        │   ├── templates/          # directory for HTML templates used by the meal planning app
        │   │   ├── recipe_detail.html   # template for displaying recipe details
        │   │   └── dashboard.html       # template for displaying the meal planning dashboard
        │   ├── tests.py            # file for unit tests for the meal planning app
        │   ├── urls.py             # file defining URL patterns for the meal planning app
        │   └── views.py            # file defining view functions for the meal planning app
        └── manage.py              # command-line utility for interacting with Django project

## 