# Bryntum Scheduler with Django

How to use the Bryntum Scheduler with Django 

## Getting Started

Clone the repo and checkout the complete app branch 

Create and activate a virtual environment 

```sh
python -m venv venv
source venv/bin/activate
```

Install Django

```sh
pip install django
```

Run migrations 

```shell
python manage.py makemigrations scheduler
python manage.py migrate 
```

Load sample data into SQLite database 

```shell
sqlite3 db.sqlite3
```

Events

```

```

Dependencies 

```

```

Resources 

```

```

Assignments

```

```

Download the Bryntum Scheduler distribution folder [here](https://customerzone.bryntum.com/)

Copy the following files and folders from the `/build` folder in the Bryntum Scheduler distribution folder and paste them into the `static/bryntum-scheduler` folder:

```
fonts
locales
scheduler.module.js
scheduler.module.js.map
scheduler.stockholm.css
scheduler.stockholm.css.map
```

## Running the app

```
python manage.py runserver localhost:8000
```

The app will be accessible at `http://localhost:8000` and you can perform Gantt CRUD operations