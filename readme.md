## Project architecture


```
meal-prep/
├── gpt_utils/
│   ├── describe_dir.py             # directory tree structure script
│   ├── private_template.py         # sensitive config settings template
│   ├── prompts.py                  # GPT prompts
│   └── update_readme.py            # update README script
├── django_app/
│   ├── PrepPilot/
│   │   ├── asgi.py                 # ASGI config
│   │   ├── settings.py             # project settings
│   │   ├── urls.py                 # project URL config
│   │   └── wsgi.py                 # WSGI config
│   ├── meal_planner/
│   │   ├── migrations/...          # database migrations
│   │   ├── models.py               # app models
│   │   ├── apps.py                 # app config
│   │   ├── admin.py                # admin interface
│   │   ├── templates/              # HTML templates
│   │   │   ├── recipe_detail.html  # recipe details template
│   │   │   └── dashboard.html      # dashboard template
│   │   ├── db_utils.py             # database utils
│   │   ├── tests.py                # unit tests
│   │   ├── urls.py                 # app URL patterns
│   │   └── views.py                # view functions
│   └── manage.py                   # Django command-line utility
├── recipes-examples.md             # recipe examples
├── start_server.sh                 # start server script
├── python_env.text                 # dependencies list
├── readme.md                       # project info and instructions
└── react_frontend/
    ├── README.md                   # frontend README
    ├── public/...                  # public assets
    ├── package-lock.json           # dependency lock file
    ├── package.json                # dependency management
    └── src/                        # frontend source
        ├── reportWebVitals.js      # web vitals report
        ├── TimeTable.css           # timetable styles
        ├── Mealdetail.js           # meal detail component
        ├── App.css                 # app styles
        ├── Mealdetail.css          # meal detail styles
        ├── index.js                # entry point
        ├── index.css               # index styles
        ├── Recipe.js               # recipe component
        ├── App.test.js             # app tests
        ├── ItemTypes.js            # item types definition
        ├── setupTests.js           # test setup
        ├── TimeTable.js            # timetable component
        └── App.js                  # main app component
```

##

## Settup steps


```
cd react_frontend
npm install
```

## Run the React app

```
cd react_frontend
npm start
```
