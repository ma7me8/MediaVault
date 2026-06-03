# MediaVault

MediaVault is a Django web application for managing a simple media catalog. The current version focuses on movies, genres, stock count, daily rental rate, release year, and descriptions. It includes a Bootstrap-based interface, Django admin management, and a basic API endpoint for movie data.

This project started as a Django course project and is being improved into a portfolio-ready media storage and stock management application.

## Features

- Movie catalog page
- Movie details page
- Genre management
- Stock tracking for each movie
- Daily rental rate field
- Description and release year fields
- Django admin dashboard
- Bootstrap 5 layout
- Basic API resource for movies
- SQLite database for local development

## Tech Stack

- Python
- Django
- Django Templates
- Bootstrap 5
- SQLite
- Tastypie API resource

## Project Structure

```text
MediaVault/
+-- MediaVault/          # Main Django project settings and URLs
+-- movies/              # Movie catalog app
+-- api/                 # API resource app
+-- templates/           # Shared templates
+-- static/              # Static files
+-- manage.py
+-- requirements.txt
+-- Pipfile
+-- Procfile
```

## Main Pages

- `/` - Home page
- `/movies/` - Movie list
- `/movies/<id>` - Movie detail page
- `/admin/` - Django admin panel
- `/api/movies/` - Movie API resource

## Getting Started

1. Clone the project or open the project folder.

2. Create and activate a virtual environment.

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies.

```bash
pip install -r requirements.txt
```

4. Run database migrations.

```bash
python manage.py migrate
```

5. Create an admin user.

```bash
python manage.py createsuperuser
```

6. Start the development server.

```bash
python manage.py runserver
```

7. Open the app in your browser.

```text
http://127.0.0.1:8000/
```

## Current Data Model

The app currently has two main models:

- `Genre`: stores the movie genre name.
- `Movie`: stores title, release year, stock count, daily rate, genre, creation date, and description.

## Roadmap

Planned improvements to make the project stronger for real use and for a CV:

- Add user authentication
- Add create, update, and delete pages for movies
- Add search and filtering
- Add pagination for the movie list
- Improve Bootstrap UI and responsive design
- Add media file uploads for posters, images, videos, or documents
- Add private user media storage
- Replace SQLite with PostgreSQL for production
- Add automated tests
- Add screenshots and deployment link
- Deploy the project online

## CV Description

Built a Django media catalog and stock management application with movie listings, genre relationships, stock tracking, Django admin integration, Bootstrap templates, and a basic API resource.

## Status

This project is currently in development. The first version works as a movie catalog and stock tracker, and future versions will expand it into a full media storage platform.
