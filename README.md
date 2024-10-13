
# Warehouse Management System - Backend

This is the backend server for the Warehouse Management System, built using Django and Django REST Framework (DRF). The backend exposes API endpoints to manage godowns, sub-godowns, and items, and includes JWT authentication and social OAuth.

## Features

- Exposes REST API endpoints to manage:
  - Godowns (warehouses)
  - Sub-godowns (sub-sections within a warehouse)
  - Items (stored in godowns or sub-godowns)
- JWT authentication for securing the API endpoints.
- Social OAuth authentication (e.g., Google OAuth) for user login.
- Provides CRUD functionality for godowns, sub-godowns, and items.
- Manages item attributes such as name, quantity, category, price, status, brand, and additional attributes like color, metal, and warranty.

## Prerequisites

- Python 3.x
- Django 3.x or later
- Django REST Framework
- pip (Python package installer)
- A virtual environment (recommended)

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/Gaurav-160/warehouse-backend.git
cd warehouse-backend
```

### 2. Create and activate a virtual environment

#### On macOS and Linux:

```bash
python3 -m venv env
source env/bin/activate
```

#### On Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install the required packages

After activating the virtual environment, install the dependencies listed in the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure the database (optional)

Update the `DATABASES` setting in `settings.py` to configure your preferred database.

### 5. Run migrations

Apply migrations to set up the database schema.

```bash
python manage.py migrate
```

### 6. Create a superuser (optional)

To access the Django admin panel, create a superuser.

```bash
python manage.py createsuperuser
```

### 7. Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

The backend API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- **Godowns:** `/warehouse/godowns/`
- **Items:** `/warehouse/items/`

Refer to the API documentation for detailed information about each endpoint.

## Authentication

- JWT Authentication is used for securing the API.
- Social OAuth login (Google) is supported for user authentication.


