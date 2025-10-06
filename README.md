# TodoAPI 📝

Welcome! This is a simple to-do list API built with Django. It's a great project for learning the basics of creating a REST API.

## ✨ Core Features

*   **User Accounts:** Create user accounts and log in.
*   **Task Management:** Create, Read, Update, and Delete your own tasks
*   **API Documentation:** An interactive Swagger UI to easily explore and test the API.

## 🛠️ Technologies Used

*   **Backend**: [Python](https://www.python.org/), [Django](https://www.djangoproject.com/)
*   **API Framework**: [Django REST Framework](https://www.django-rest-framework.org/)
*   **Authentication**: [Djoser](https://djoser.readthedocs.io/en/latest/) 
*   **API Schema**: [drf-yasg](https://drf-yasg.readthedocs.io/en/latest/) (for generating a Swagger/OpenAPI schema.)
*   **Database**: [SQLite](https://www.sqlite.org/index.html)

## 🚀 Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8+

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/Tornam/TodoAPI.git
    cd TodoAPI
    ```

2.  **Create and activate a virtual environment:**
    A virtual environment keeps your project's dependencies separate from other projects.
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a file named `.env` in the project root directory (the same folder as `manage.py`). Your `.env` file should look like this:
    ```
    SECRET_KEY='your-super-secret-key-goes-here'
    DEBUG=True

    # You can generate the `SECRET_KEY` by running:
    # python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

5.  **Apply database migrations:**
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

The API will now be running at `http://127.0.0.1:8000/`.

## 📖 Using the API

*   **Swagger UI:** `http://127.0.0.1:8000/docs/swagger/`
*   **Redoc:** `http://127.0.0.1:8000/docs/redoc/`

### 1. Create a User
Go to the Swagger UI:
*   **`POST /auth/users/`**: Create a new user.
    *   **Request Body:**
        ```json
        {
          "username": "testuser",
          "password": "strong-password"
        }
        ```

### 2. Get an Authentication Token
To access protected endpoints (like your tasks), you need to log in to get a token.
*   **`POST /auth/token/login/`**: Log in and receive an auth token.
    *   **Request Body:**
        ```json
        {
          "username": "testuser",
          "password": "strong-password"
        }
        ```
    *   **Success Response:** You'll get a response with your token, like `{"auth_token": "your-token-string"}`.

### 3. Make Authenticated Requests
To use your token, click the "Authorize" button at the top of the Swagger page. In the popup, type `Token` followed by a space and your token string.

Example: `Token your-token-string`

Now you can access the task endpoints!

### Task Endpoints

*   **`GET /api/tasks/`**: Get a list of *your* to-do items.
*   **`POST /api/tasks/`**: Create a new to-do item for yourself.
    *   **Request Body:**
        ```json
        {
            "title": "My first task",
            "description": "Learn how to use the API."
        }
        ```
*   **`GET /api/tasks/{id}/`**: Get a single one of your tasks.
*   **`PUT /api/tasks/{id}/`**: Update one of your tasks.
*   **`PATCH /api/tasks/{id}/`**: Partially update one of your tasks.
*   **`DELETE /api/tasks/{id}/`**: Delete one of your tasks.
