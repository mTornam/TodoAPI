# Todo API

A simple yet powerful RESTful API for managing Todos and Categories, built with Django and Django REST Framework.

## Features

- **User Authentication**: Token-based authentication for secure access.
- **User Management**: Endpoints for user registration and login/logout powered by `Djoser`.
- **CRUD Operations**: Full Create, Read, Update, and Delete functionality for Todos and Categories.
- **Filtering & Ordering**: Filter Todos by completion status, category, and date. Order them by title, creation date, or category.
- **Pagination**: Custom pagination for handling large datasets.
- **API Documentation**: Auto-generated, interactive API documentation with Swagger UI and ReDoc.

## API Documentation

Once the server is running, you can access the interactive API documentation at:

- **Swagger UI**: `/api/docs/`
- **ReDoc**: `/api/docs/redoc/`

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Pip (Python package installer)
- A running MySQL server (or you can switch to SQLite in `settings.py`)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone <your-repo-url>
    cd todoApi
    ```

2.  **Create and activate a virtual environment:**
    ```sh
    # For Windows
    python -m venv venv
    .\venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    Install the packages:
    ```sh
    pip install -r requirements.txt
    ```

4.  **Configure Database:**
    Update the `DATABASES` setting in `todoApi/settings.py` with your MySQL credentials. 

5.  **Create & Apply database migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```
    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints & Usage

All endpoints require a `Token` in the `Authorization` header: `Authorization: Token <your_auth_token>`.

### Authentication

- `POST /auth/users/`: Register a new user.
- `POST /auth/token/login/`: Obtain an authentication token.
- `POST /auth/token/logout/`: Log out and invalidate the token.

### Categories
- `GET, POST /api/categories/`: List all categories or create a new one.
- `GET, PUT, PATCH, DELETE /api/categories/<id>/`: Retrieve, update, or delete a specific category.

### Todos
- `GET, POST /api/todos/`: List all todos or create a new one. Supports filtering and ordering.
  - Example: `GET /api/todos/?completed=true&ordering=title`
- `GET, PUT, PATCH, DELETE /api/todos/<id>/`: Retrieve, update, or delete a specific todo.