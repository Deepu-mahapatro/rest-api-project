
# 🚀 REST API Learning Project

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge-Django_REST_Framework-API-BA1400?style=for-the-badge" alt="Django REST Framework">
  <img src="https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Postman-API_Testing-FF6C37?style=for-the-badge&logo=postman&logoColor=white" alt="Postman">
  <img src="https://img.shields.io/badge/Git-GitHub-F05032?style=for-the-badge&logo=git&logoColor=white" alt="Git">
</p>

<p align="center">
  <b>A practical REST API learning project focused on HTTP methods, CRUD operations, validation, filtering, pagination, and API design using Django REST Framework and MySQL.</b>
</p>

---

## 📌 About the Project

This project was developed to understand **REST API fundamentals through practical implementation**.

It uses Django REST Framework to build a Product API and MySQL to store product data. API requests and responses are tested using Postman.

The project focuses on understanding how a client communicates with a backend, how requests are processed, how data is validated, and how the server returns structured JSON responses.

## 🎯 Project Objectives

- Understand REST principles and HTTP methods.
- Build REST endpoints using Django REST Framework.
- Implement CRUD operations with MySQL.
- Understand Django models, serializers, views, and ORM.
- Work with path parameters and query parameters.
- Implement filtering, searching, and pagination.
- Validate input and handle API errors.
- Understand URL-based API versioning and backward compatibility.
- Test endpoints and responses using Postman.
- Document the project structure and request lifecycle.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Backend programming |
| Django 5.2 | Web framework |
| Django REST Framework | REST API development |
| MySQL | Relational database |
| Django ORM | Database operations |
| Postman | API testing |
| Git and GitHub | Version control |
| VS Code | Development environment |

---

## 🏗️ Architecture

```text
                 ┌─────────────────────┐
                 │       Client        │
                 │   Postman / HTTP    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Django URLs      │
                 │  config/urls.py     │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │   Product Views     │
                 │  products/views.py  │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Serializer      │
                 │ products/serializers│
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │     Django ORM      │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │       MySQL         │
                 │   Product Records   │
                 └─────────────────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    JSON Response    │
                 └─────────────────────┘
```

### Core Principle

> The client sends an HTTP request, Django processes it, the ORM interacts with MySQL when necessary, and the API returns an appropriate response.

---

## ⚡ Features Implemented

| Feature | Description |
|---|---|
| Project Setup | Django configuration and environment variables |
| Health Check | Endpoint to check API availability |
| Create | Add a new product |
| Read | Retrieve all products or a single product |
| Update | Full update using PUT |
| Partial Update | Update selected fields using PATCH |
| Delete | Remove a product |
| Path Parameters | Retrieve or modify a product by ID |
| Filtering | Filter products by minimum and maximum price |
| Searching | Search product names and descriptions |
| Pagination | Page selection and configurable page size |
| Input Validation | Validate product data and query parameters |
| Error Handling | Return structured errors for handled failures |
| API Versioning | URL prefixes for V1 and V2 |
| Manual Testing | Test requests and responses using Postman |

---

## 🌐 API Endpoints

The local development base URL is:

```text
http://127.0.0.1:8000
```

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/health/` | Check API availability |
| GET | `/api/v1/products/` | Retrieve products |
| POST | `/api/v1/products/` | Create a product |
| GET | `/api/v1/products/{id}/` | Retrieve a product by ID |
| PUT | `/api/v1/products/{id}/` | Update a product |
| PATCH | `/api/v1/products/{id}/` | Partially update a product |
| DELETE | `/api/v1/products/{id}/` | Delete a product |

The same URL structure is available under `/api/v2/`.

**Versioning note:** V1 and V2 currently use the same URL configuration and implementation. Separate behavior for V2 has not been implemented.

---

## 🔎 Filtering, Searching, and Pagination

### Filter by price

```http
GET /api/v1/products/?min_price=100
```

```http
GET /api/v1/products/?max_price=1000
```

```http
GET /api/v1/products/?min_price=100&max_price=1000
```

### Search products

```http
GET /api/v1/products/?search=laptop
```

Searches product names and descriptions.

### Pagination

```http
GET /api/v1/products/?page=1&page_size=10
```

- `page`: Page number.
- `page_size`: Number of products requested per page, capped at 100.

### Combine query parameters

```http
GET /api/v1/products/?search=laptop&min_price=100&page=1&page_size=10
```

The response includes product data and pagination metadata, such as total count, current page, total pages, and navigation information.

---

## 🔄 Request Lifecycle

A typical API request follows this flow:

1. The client sends an HTTP request.
2. Django matches the URL and selects the appropriate view.
3. The view processes the request.
4. The serializer validates incoming data or converts model data into a response representation.
5. The Django ORM interacts with MySQL when database access is required.
6. Django REST Framework returns a JSON response with an appropriate HTTP status code.

```text
Client
  ↓
HTTP Request
  ↓
URL Routing
  ↓
View
  ↓
Serializer / Validation
  ↓
Django ORM
  ↓
MySQL
  ↓
JSON Response
```

---

## 🧪 Testing with Postman

The endpoints were manually tested using Postman.

Testing includes:

- Health check.
- Product creation and retrieval.
- Full and partial updates.
- Product deletion.
- Filtering by price.
- Searching by name and description.
- Pagination and combined query parameters.
- Invalid input and error responses.
- Requests using V1 and V2 URL prefixes.

Example request:

```http
GET http://127.0.0.1:8000/api/v1/products/?page=1&page_size=10
```

Check the HTTP status code, response body, and database changes where applicable.

---

## 📁 Project Structure

```text
rest-api-project/
│
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── products/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── exceptions.py
│
├── docs/
│   ├── 01-project-overview.md
│   ├── 02-rest-api-fundamentals.md
│   ├── 03-api-architecture-and-flow.md
│   ├── 04-endpoints-and-usage.md
│   └── 05-validation-versioning-and-limitations.md
│
├── .env.example
├── .gitignore
├── requirements.txt
├── manage.py
└── README.md
```

**Note:** The diagram shows the main application files. Your local `venv/` directory is excluded from Git, and `.env` must remain untracked.

### Important Files

| File | Responsibility |
|---|---|
| `config/settings.py` | Django and database configuration |
| `config/urls.py` | Main URL routing and API version prefixes |
| `products/models.py` | Product model and database constraints |
| `products/serializers.py` | Serialization and input validation |
| `products/views.py` | CRUD operations, filtering, searching, pagination, and responses |
| `products/urls.py` | Product endpoint definitions |
| `products/exceptions.py` | Custom REST framework exception handling |
| `requirements.txt` | Python dependencies |
| `.env.example` | Example environment variable names |
| `.gitignore` | Excludes secrets and generated files |
| `docs/` | Detailed project documentation |

---

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd rest-api-project
```

Replace `<your-repository-url>` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure environment variables

Create a local `.env` file in the project root using `.env.example` as a reference.

Configure the Django secret key, debug setting, and MySQL connection values according to the variable names used in `config/settings.py`.

Example structure:

```env
DJANGO_SECRET_KEY=replace-with-your-own-secret-key
DJANGO_DEBUG=True

DB_NAME=product_api_db
DB_USER=your_mysql_username
DB_PASSWORD=your_mysql_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

**Important:** These variable names must match your actual Django settings. Use your own local credentials, and never commit `.env` to GitHub.

### 5. Prepare the MySQL database

Make sure MySQL is running and the configured database exists.

Create the database if necessary, using your configured database name.

### 6. Apply migrations

```bash
python manage.py migrate
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API is now available at:

```text
http://127.0.0.1:8000/api/v1/
```

Test the health endpoint:

```text
http://127.0.0.1:8000/api/v1/health/
```

---

## 📚 Documentation

The `docs/` directory contains focused documentation for the project.

| Document | Description |
|---|---|
| [Project Overview](docs/01-project-overview.md) | Purpose, objectives, technology stack, and scope |
| [REST API Fundamentals](docs/02-rest-api-fundamentals.md) | REST principles, HTTP methods, status codes, and JSON |
| [Architecture and Request Flow](docs/03-api-architecture-and-flow.md) | Project structure and request lifecycle |
| [Endpoints and Usage](docs/04-endpoints-and-usage.md) | Endpoint reference, query parameters, and Postman usage |
| [Validation, Versioning, and Limitations](docs/05-validation-versioning-and-limitations.md) | Validation, error handling, versioning, and future improvements |

---

## 🎓 Learning Outcomes

Through this project, the following concepts were practiced:

- REST API fundamentals.
- HTTP methods, headers, status codes, and JSON.
- Django models, views, serializers, and ORM.
- CRUD operations with MySQL.
- Path parameters and query parameters.
- Filtering, searching, and pagination.
- Input validation and error handling.
- API versioning and backward compatibility.
- Request lifecycle and backend architecture.
- Manual API testing using Postman.
- Environment variable management and Git hygiene.

---

## 🚧 Project Scope and Limitations

This project focuses on the fundamentals of REST API development. It is a learning project, not a complete production-ready service.

The following are outside the current scope:

- Automated API tests and CI/CD.
- Swagger/OpenAPI documentation.
- Advanced database optimization and dedicated transaction workflows.
- Production authentication and role-based authorization.
- Comprehensive rate limiting and monitoring.
- Production deployment configuration.
- Independent implementations for V1 and V2.

These topics can be added as future improvements.

---

## 🧠 Final Mental Model

```text
             CLIENT
                │
                ▼
          HTTP REQUEST
                │
                ▼
          DJANGO ROUTING
                │
                ▼
              VIEW
                │
                ▼
       SERIALIZER / VALIDATION
                │
                ▼
           DJANGO ORM
                │
                ▼
             MySQL
                │
                ▼
         JSON RESPONSE
                │
                ▼
             CLIENT
```

The key idea is to understand not only how to create endpoints, but also **why each component exists and how data moves through the backend**.

---

## ⭐ Key Takeaway

> This project provides a practical foundation for designing, implementing, testing, and documenting REST APIs using Django REST Framework and MySQL.
