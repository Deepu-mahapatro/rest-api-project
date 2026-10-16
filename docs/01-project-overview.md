
# REST API Project — Overview

## 1. Introduction

This project is a basic REST API built using Django REST Framework and MySQL. It demonstrates how clients communicate with a backend through HTTP requests and receive structured JSON responses.

The goal is to understand REST API concepts through practical implementation rather than theory alone.

## 2. Objectives

- Understand REST principles and HTTP methods.
- Implement CRUD operations with MySQL.
- Learn Django models, serializers, views, and ORM.
- Handle path parameters and query parameters.
- Implement filtering, searching, and pagination.
- Validate input and handle API errors.
- Understand API versioning and backward compatibility.
- Test API endpoints using Postman.

## 3. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Django | Web framework |
| Django REST Framework | REST API development |
| MySQL | Relational database |
| Django ORM | Database interaction |
| Postman | API testing |
| Git and GitHub | Version control and hosting |

## 4. Implemented Features

- **Project setup:** Django configuration, environment variables, MySQL integration, and health check.
- **CRUD operations:** Create, retrieve, update, partially update, and delete products.
- **Request parameters:** Path parameters and optional query parameters.
- **Filtering and searching:** Filter products by price and search product names or descriptions.
- **Pagination:** Page selection, configurable page size, total count, and navigation metadata.
- **Validation and error handling:** Serializer validation, custom error responses, and appropriate HTTP status codes.
- **API versioning:** URL prefixes `/api/v1/` and `/api/v2/`, with an introduction to backward compatibility.
- **Manual testing:** API requests and responses verified using Postman.

## 5. API Endpoint Summary

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/api/v1/health/` | Check API availability |
| GET | `/api/v1/products/` | List products |
| POST | `/api/v1/products/` | Create a product |
| GET | `/api/v1/products/{id}/` | Retrieve a product |
| PUT | `/api/v1/products/{id}/` | Update a product |
| PATCH | `/api/v1/products/{id}/` | Partially update a product |
| DELETE | `/api/v1/products/{id}/` | Delete a product |

The same endpoint structure is available under `/api/v2/`.

## 6. Example Query Parameters

```text
/api/v1/products/?min_price=100
/api/v1/products/?search=laptop
/api/v1/products/?page=1&page_size=10
/api/v1/products/?search=laptop&min_price=100&page=1&page_size=10
```

These examples demonstrate filtering, searching, pagination, and combining query parameters.

## 7. Request Lifecycle

1. Client sends an HTTP request.
2. Django routes the request to the appropriate view.
3. The view processes the request and uses the serializer when needed.
4. The Django ORM interacts with MySQL.
5. The API returns a JSON response with an appropriate HTTP status code.

## 8. Project Scope

This project focuses on the fundamentals of REST API development. Advanced topics such as database query optimization, dedicated transaction workflows, automated testing, Swagger/OpenAPI documentation, and production monitoring are outside the current scope.

## 9. Conclusion

This project provides a practical foundation for understanding REST APIs, database integration, request handling, validation, and response generation using Django REST Framework.
```
