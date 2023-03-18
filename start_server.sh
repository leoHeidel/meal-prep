#!/bin/bash

# Activate the conda environment
source activate meal-prep

# Start the Django development server
cd django/
python manage.py runserver

