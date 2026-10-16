
# API Architecture and Request Flow

## 1. Overview

This project uses Django REST Framework (DRF) to handle HTTP requests, validate data, perform database operations, and return JSON responses.

MySQL stores product data, while the Django ORM provides a Python interface for interacting with the database.

## 2. Project Structure

```text
rest-api-project/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── products/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   ├── exceptions.py
│   └── admin.py
├── docs/
│   ├── 01-project-overview.md
│   ├── 02-rest-api-fundamentals.md
│   ├── 03-api-architecture-and-flow.md
│   ├── 04-endpoints-and-usage.md
│   └── 05-validation-versioning-and-limitations.md
├── .env
├── .env.example
├── .gitignore
├── manage.py
├── requirements.txt
└── README.md
```

**Note:** The structure above represents the main project files. Some files, such as `__init__.py`, are generated during project setup. The `venv/` directory is excluded from Git.

## 3. Responsibilities of Each Component

| Component | Responsibility |
|---|---|
| `manage.py` | Runs Django management commands |
| `config/settings.py` | Configures Django, database settings, installed apps, and REST framework settings |
| `config/urls.py` | Defines the main URL routes, including API version prefixes |
| `products/urls.py` | Maps product endpoints to their corresponding views |
| `products/models.py` | Defines the product database structure and model constraints |
| `products/serializers.py` | Converts model data to JSON-compatible representations and validates incoming data |
| `products/views.py` | Processes requests, applies business logic, and returns responses |
| `products/exceptions.py` | Defines the custom REST framework exception handler |
| `products/migrations/` | Stores database schema changes |
| `.env` | Stores local configuration and sensitive environment variables |
| `.env.example` | Documents the environment variables required to configure the project |
| `requirements.txt` | Lists Python package dependencies |
| `docs/` | Contains project documentation |

## 4. Request Lifecycle

Consider a client requesting:

```http
GET /api/v1/products/5/
```

The request passes through these components:

1. **Client:** Sends an HTTP request using Postman or another application.
2. **Main URL configuration:** `config/urls.py` matches the `/api/v1/` prefix and forwards the remaining path to `products/urls.py`.
3. **App URL configuration:** `products/urls.py` matches `products/5/` and selects the product detail view.
4. **View:** `products/views.py` reads the product ID and determines the required operation.
5. **ORM and database:** The Django ORM retrieves the matching product from MySQL.
6. **Serializer:** `products/serializers.py` converts the model instance into JSON-compatible data.
7. **Response:** Django REST Framework returns the response with an appropriate HTTP status code.

The exact path varies by operation. For example, a POST request also validates incoming data and saves a new product.

## 5. Example: Creating a Product

A client sends:

```http
POST /api/v1/products/
Content-Type: application/json
```

Request body:

```json
{
  "name": "Laptop",
  "description": "A portable computer",
  "price": "55000.00",
  "stock": 10
}
```

The process is:

1. Django routes the request to the product collection view.
2. The view passes the submitted data to `ProductSerializer`.
3. The serializer validates the input.
4. If valid, the serializer saves the product through the Django ORM.
5. The ORM inserts the record into MySQL.
6. The API returns the created product and a success status, typically `201 Created`.

If validation fails, the API returns an error response instead of creating the product.

## 6. How the ORM Connects Django to MySQL

The ORM allows developers to work with database records using Python objects rather than writing SQL for every operation.

Example:

```python
# Retrieve all products
products = Product.objects.all()

# Retrieve one product
product = Product.objects.get(id=5)

# Create a product
Product.objects.create(
    name="Laptop",
    description="A portable computer",
    price=55000.00,
    stock=10,
)
```

These examples illustrate the ORM interface. The actual API uses its model and serializer logic to perform the relevant operations.

## 7. Error Handling Flow

When a request contains invalid data or refers to a missing resource, the application should return a meaningful error response.

- **Serializer validation:** Detects invalid input before saving data.
- **View-level error handling:** Handles application-specific errors, such as invalid query parameters or missing products.
- **Custom exception handler:** Standardizes many exceptions handled by Django REST Framework.

The exception handler does not automatically handle every possible Python error or unmatched URL. Unexpected server errors still require appropriate debugging and handling.

## 8. Key Takeaway

The main request flow is:

**Client → URL Routing → View → Serializer → ORM → MySQL → JSON Response**

The view coordinates the operation, the serializer handles data representation and validation, and the ORM communicates with the database. Together, these components keep the API organized and maintainable.
