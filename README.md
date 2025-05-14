# Library System API

A simple Django REST Framework (DRF) based Library System that allows managing books using both APIView and ModelViewSet approaches. The project provides endpoints to list, create, update, and delete books, and includes a sample SQLite database and a Postman collection for testing.

## Features

- List all books
- Add new books
- Retrieve, update, or delete a book by ID
- Two types of API:
  - APIView (custom logic)
  - ModelViewSet (router-based CRUD)
- Browsable API with DRF
- Postman collection included for testing

## Requirements

- Python 3.x
- Django 4.x
- Django REST Framework
- SQLite (included for testing)

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/TukaHeba/DRF.git
2. Navigate to the project directory:
   ```bash
   cd library
3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate  # Windows: env\Scripts\activate
4.	Install dependencies:
   ```bash
    pip install django djangorestframework
5.	Run migrations and start the server:
   ```bash
    python manage.py migrate
    python manage.py runserver

You can access postman collection [here](https://documenter.getpostman.com/view/34424205/2sB2qUnjwV).