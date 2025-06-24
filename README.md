# Ciao Book Shop

A Django-based online bookstore application.

## Features

- Browse and search books
- User registration and authentication
- Shopping cart management
- Order processing and history
- Admin panel for book management
- Stock tracking

## Setup

1. Install Python 3.x
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Create superuser:
   ```
   python manage.py createsuperuser
   ```
5. Run server:
   ```
   python manage.py runserver
   ```

## Usage

- Visit `http://127.0.0.1:8000/` to browse books
- Register an account to add books to cart and place orders
- Admin panel available at `/admin/`

## Technologies

- Django
- SQLite
- HTML/CSS/JavaScript