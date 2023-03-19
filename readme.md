## Project architecture


```
meal-prep/
├── gpt_utils/
│   ├── describe_dir.py             # script to print a directory tree structure
│   ├── private_template.py         # template for sensitive configuration settings (not committed to version control)
│   ├── update_readme.py            # script to automatically update the project README file
├── django_app/                     # directory for the Django project
│   ├── PrepPilot/                  # directory for Django project configuration
│   │   ├── asgi.py                 # ASGI configuration
│   │   ├── settings.py             # project-level settings
│   │   ├── urls.py                 # project-level URL configuration
│   │   └── wsgi.py                 # WSGI configuration
│   ├── meal_planner/               # directory for the meal planning app
│   │   ├── migrations/             # directory for Django database migrations
│   │   │   ├── 0002_day_recipes.py # migration for adding the ManyToManyField for recipes in Day model
│   │   │   ├── 0003_remove_recipe_instructions_instruction.py # migration for removing instructions field from Recipe model
│   │   │   └── 0001_initial.py     # migration for creating the Week, Day, Recipe, and Ingredient models
│   │   ├── models.py               # file defining the Week, Day, Recipe, and Ingredient models
│   │   ├── apps.py                 # file defining the MealPlannerConfig app configuration class
│   │   ├── admin.py                # file defining the admin interface for the Week, Day, Recipe, and Ingredient models
│   │   ├── templates/              # directory for HTML templates used by the meal planning app
│   │   │   ├── recipe_detail.html  # template for displaying recipe details
│   │   │   └── dashboard.html      # template for displaying the meal planning dashboard
│   │   ├── db_utils.py             # utility functions for working with the database
│   │   ├── tests.py                # file for unit tests for the meal planning app
│   │   ├── urls.py                 # file defining URL patterns for the meal planning app
│   │   └── views.py                # file defining view functions for the meal planning app
│   └── manage.py                   # command-line utility for interacting with Django project
├── recipes-examples.md             # file with recipe examples for testing
├── start_server.sh                 # shell script to activate conda environment and start Django server
├── python_env.text                 # text file containing the list of dependencies for the project environment
└── readme.md                       # file with instructions and info about the project
```

##



In my models.py file change the Recipe class so that the instruction are a list instead of a single field. Currently in model we have:

You are a helpful coding assistant, we are currently coding a meal planer app. This is the current architecture of the project: