# Bryntum Scheduler with Django

This repository contains the starter code for building a Bryntum Scheduler using Django. The code for the completed app is in the `complete-app` branch. To run this app, clone this repo and switch to the `complete-app` branch before following the steps below.

## Setup

Create and activate a virtual environment in the root folder:

```sh
python -m venv venv
source venv/bin/activate
```

Inside the virtual environment, install Django:

```sh
pip install django
```

Once Django is installed, make and run the migrations:

```sh
python manage.py makemigrations scheduler
python manage.py migrate 
```

Then add some sample data to the SQLite database:

```sh
sqlite3 db.sqlite3
```

Events:

```sql
INSERT INTO events (id, startDate, endDate, name, durationUnit) 
VALUES
    (1, '2024-02-19 09:00:00', '2024-02-19 10:30:00', 'Conference call', 'day'),
    (2, '2024-02-19 11:30:00', '2024-02-19 13:00:00', 'Sprint planning', 'day'),
    (3, '2024-02-19 12:00:00', '2024-02-19 13:30:00', 'Team meeting', 'day'),
    (4, '2024-02-19 14:00:00', '2024-02-19 15:45:00', 'Client presentation', 'day'),
    (5, '2024-02-19 15:30:00', '2024-02-19 16:45:00', 'Project review', 'day'),
    (6, '2024-02-19 17:00:00', '2024-02-19 18:30:00', 'Marketing discussion', 'day'),
    (7, '2024-02-19 08:00:00', '2024-02-19 09:00:00', 'Breakfast Briefing', 'day'),
    (8, '2024-02-19 16:00:00', '2024-02-19 17:45:00', 'Technology Update', 'day'),
    (9, '2024-02-19 14:15:00', '2024-02-19 15:15:00', 'HR Update', 'day'),
    (10, '2024-02-19 11:00:00', '2024-02-19 12:45:00', 'Financial Planning', 'day');
```

Dependencies:

```sql
INSERT INTO dependencies (id, `from`, `to`)
VALUES
  (1, 1, 2),
  (2, 3, 4);
```

Resources:

```sql
INSERT INTO resources (id, name)
VALUES
  (1, 'Peter'),
  (2, 'Kate'),
  (3, 'Winston'),
  (4, 'Joshua'),
  (5, 'James'),
  (6, 'Leanne');
```

Assignments:

```sql
INSERT INTO assignments (id, eventId, resourceId)
VALUES
  (1, 1, 1),
  (2, 2, 1),
  (3, 3, 3),
  (5, 4, 3),
  (6, 5, 6),
  (7, 6, 2),
  (8, 7, 4),
  (9, 8, 4),
  (10, 9, 5),
  (11, 10, 5);
```

Download the Bryntum Scheduler distribution folder [here](https://customerzone.bryntum.com/).

If you don't have a license for the Bryntum Scheduler, download the trial version [here](https://bryntum.com/download/?product=scheduler). Copy the following files and folders from the `/build` folder in the Bryntum Scheduler distribution folder and paste them into the `static/bryntum-scheduler` folder:

```
fonts
locales
scheduler.module.js
scheduler.module.js.map
scheduler.stockholm.css
scheduler.stockholm.css.map
```

## Running the application

Run the development server with:

```sh
python manage.py runserver localhost:8000
```

The app will be accessible at `http://localhost:8000` and you can perform Scheduler CRUD operations