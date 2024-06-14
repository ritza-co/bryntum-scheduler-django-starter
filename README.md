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

Dependencies 

```sql
INSERT INTO dependencies (id, `from`, `to`)
VALUES
  (1, 1, 2),
  (2, 3, 4);
```

Resources 

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

Assignments

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