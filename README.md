# Movie Watchlist

Minimal Django app for managing a personal movie watchlist: create movies, assign genres, and track watch status in a user dashboard.

## Features

- User authentication (register, login, logout)
- Movie CRUD (create, edit, delete, detail)
- Genre list
- Personal dashboard with watch status (plan / watching / watched) and optional rating
- Bootstrap-based UI + custom styling

## Tech Stack

- Python
- Django
- Bootstrap 5

## Installation

1. Create and activate a virtual environment
   - Windows (PowerShell): `python -m venv venv; .\\venv\\Scripts\\Activate.ps1`
   - macOS/Linux: `python -m venv venv && source venv/bin/activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Create `.env` (see below)
4. Run migrations: `python manage.py migrate`
5. (Optional) Create admin user: `python manage.py createsuperuser`
6. Run server: `python manage.py runserver`
7. Open: `http://127.0.0.1:8000/movie_watchlist/`

## Environment Variables

This project uses `python-decouple` to load settings from `.env` (see `config/settings.py`).

Example `.env`:

```env
SECRET_KEY=replace-me
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost
```

- `SECRET_KEY`: Django secret key
- `DEBUG`: `True`/`False`
- `ALLOWED_HOSTS`: comma-separated hosts

## Screenshots

<img width="1919" height="1030" alt="image" src="https://github.com/user-attachments/assets/2b6d38bb-be21-4bff-818a-5d14dd6f1b52" />
<img width="1898" height="1012" alt="image" src="https://github.com/user-attachments/assets/0b650fb2-90ff-4124-a92e-2e07a939e2c0" />
<img width="1919" height="1025" alt="image" src="https://github.com/user-attachments/assets/d2de7030-8516-4bd3-a3d6-fa65c14aad15" />


