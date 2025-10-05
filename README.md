# TodoAPI 📝

A simple RESTful API for managing a to-do list, built with Django and Django REST Framework.

## ✨ Core Features

*   **CRUD Operations:** Full support for Creating, Reading, Updating, and Deleting to-do items.

*   **Browsable API:** User-friendly interface provided by Django REST Framework for easy interaction and testing in the browser.

## 🛠️ Technologies Used

*   **Backend**: [Python](https://www.python.org/), [Django](https://www.djangoproject.com/)
*   **API Framework**: [Django REST Framework](https://www.django-rest-framework.org/)
*   **Authentication**: [Djoser](https://djoser.readthedocs.io/en/latest/) & [Simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/) for token-based authentication.
*   **API Schema**: [drf-spectacular](https://drf-spectacular.readthedocs.io/en/latest/) for generating OpenAPI 3 schemas.
*   **Database**: [SQLite](https://www.sqlite.org/index.html) (default, easily configurable)

## 🚀 Getting Started

> **Security Note**
> This project is configured to load some credentials (like `SECRET_KEY`) from environment variables.

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone https://github.com/your-username/TodoAPI.git
    cd TodoAPI
    ```

2.  **Create and activate a virtual environment:**
    *   On Windows:
        ```sh
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```sh
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**

    Create a `.env` file in the project root directory (same folder as `manage.py`). Then, generate a new secret key and add it to the file.

    You can generate a key using Django's built-in management command:
    ```sh
    python manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

    Your `.env` file should look like this:
    ```
    SECRET_KEY='your-newly-generated-secret-key'
    DEBUG=True
    ```

5.  **Apply database migrations:**
    ```sh
    python manage.py migrate
    ```

6.  **Run the development server:**
    ```sh
    python manage.py runserver
    ```

The API will be available at `http://127.0.0.1:8000/`.

## 📖 API Endpoints

Here are the available endpoints. The base URL is `/api/`.

### Todos (`/tasks/`)

*   **`GET /api/tasks/`**
    *   **Description:** Retrieve a list of all to-do items.
    *   **Success Response (200 OK):**
        ```json
        [
            {
                "id": 1,
                "title": "Learn Django",
                "description": "Read the official Django documentation.",
                "completed": false
            },
            {
                "id": 2,
                "title": "Build an API",
                "description": "Create a simple Todo API.",
                "completed": true
            }
        ]
        ```

*   **`POST /api/tasks/`**
    *   **Description:** Create a new to-do item.
    *   **Request Body:**
        ```json
        {
            "title": "Write a README",
            "description": "Document the API endpoints."
        }
        ```
    *   **Success Response (201 Created):** The newly created to-do item object.

### Single Todo (`api/tasks/<id>/`)

*   **`GET /api/tasks/<id>/`**: Retrieve a single to-do item by its ID.
*   **`PUT /api/tasks/<id>/`**: Update a to-do item. Requires all fields.
*   **`PATCH /api/tasks/<id>/`**: Partially update a to-do item. Only include the fields you want to change.
*   **`DELETE /api/tasks/<id>/`**: Delete a to-do item.

