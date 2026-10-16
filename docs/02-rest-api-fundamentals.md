
# REST API Fundamentals

## 1. What Is a REST API?

REST (Representational State Transfer) is an architectural style for designing network-based applications.

A REST API allows a client, such as a web application or mobile app, to communicate with a server using HTTP requests and receive responses, commonly in JSON format.

**Example:** A client requests a list of products, and the server returns product data as JSON.

## 2. Resources and Endpoints

A resource represents an entity or object managed by the API, such as a product, user, or order.

An endpoint is a URL through which a client accesses a resource.

Example:

```text
GET /api/v1/products/
GET /api/v1/products/5/
```

- `/api/v1/products/` represents the product collection.
- `/api/v1/products/5/` represents the product with ID `5`.

REST APIs generally use nouns to represent resources rather than action-based URL names.

## 3. HTTP Methods

HTTP methods define the operation a client wants to perform.

| Method | Purpose | Example |
|---|---|---|
| GET | Retrieve data | Get all products |
| POST | Create a resource | Create a product |
| PUT | Replace/update a resource | Update a product |
| PATCH | Partially update a resource | Update its price |
| DELETE | Delete a resource | Delete a product |

The method and endpoint together describe the requested operation.

## 4. HTTP Status Codes

Status codes communicate the result of a request.

| Status Code | Meaning | Typical Use |
|---|---|---|
| 200 OK | Request successful | Retrieve or update data |
| 201 Created | Resource created | Successful POST |
| 204 No Content | Successful request without a response body | Successful DELETE |
| 400 Bad Request | Invalid request | Validation failure |
| 404 Not Found | Resource not found | Invalid product ID |
| 405 Method Not Allowed | HTTP method unsupported | Using an unsupported method |
| 500 Internal Server Error | Unexpected server error | Unhandled server-side failure |

The exact status code depends on how the endpoint handles the request.

## 5. JSON Request and Response

JSON (JavaScript Object Notation) is a common format for exchanging structured data between clients and servers.

Example request body:

```json
{
  "name": "Laptop",
  "description": "A portable computer",
  "price": "55000.00",
  "stock": 10
}
```

Example response:

```json
{
  "id": 5,
  "name": "Laptop",
  "description": "A portable computer",
  "price": "55000.00",
  "stock": 10
}
```

The server validates the submitted data, processes the request, and returns an appropriate response.

## 6. HTTP Headers

Headers provide additional information about a request or response.

Common examples:

| Header | Purpose |
|---|---|
| `Content-Type` | Describes the format of the request or response body |
| `Accept` | Indicates the response formats the client can accept |
| `Authorization` | Carries authentication credentials when required |

For JSON requests, clients commonly send:

```http
Content-Type: application/json
Accept: application/json
```

## 7. Safe and Idempotent Methods

**Safe methods:** Methods that are intended to retrieve information without changing the server's application state. GET is the main example.

**Idempotent methods:** Methods for which repeating the same request has the same intended effect on server state as performing it once.

| Method | Safe? | Idempotent? |
|---|---|---|
| GET | Yes | Yes |
| POST | No | Generally no |
| PUT | No | Yes |
| PATCH | No | Depends on the operation |
| DELETE | No | Yes |

For example, repeating a DELETE request should leave the resource deleted, even if a later request returns `404 Not Found`.

Idempotency describes the intended effect on server state, not whether every response is identical.

## 8. Core REST Principles

REST is associated with these architectural constraints:

- **Client–server:** The client handles the user interface, while the server manages data and business logic.
- **Statelessness:** Each request contains the information needed to process it; the server does not rely on stored client-session context between requests.
- **Cacheability:** Responses can indicate whether they may be cached.
- **Uniform interface:** Resources are accessed through consistent conventions.
- **Layered system:** Intermediaries such as proxies or gateways may exist between the client and server.
- **Code on demand (optional):** A server may provide executable code to a client.

A REST API does not become RESTful merely by using JSON and HTTP. Its design should follow the relevant REST constraints.

## 9. Key Takeaway

REST API fundamentals help us design consistent endpoints, choose appropriate HTTP methods and status codes, exchange JSON data, and understand how clients communicate with servers.

In this project, these concepts are applied through product endpoints implemented with Django REST Framework and MySQL.
