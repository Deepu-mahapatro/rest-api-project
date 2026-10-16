
# API Endpoints and Usage

## 1. Base URLs

The API supports two URL prefixes:

```text
/api/v1/
/api/v2/
```

Examples below use `/api/v1/`. The same endpoint structure is available under `/api/v2/`.

**Important:** Both versions currently use the same URL configuration, views, and behavior. Separate version implementations have not been created.

## 2. Health Check

Checks whether the API health endpoint is responding.

| Method | Endpoint |
|---|---|
| GET | `/api/v1/health/` |

Example request:

```http
GET /api/v1/health/
```

A successful request returns a success response according to the implemented health-check view.

## 3. Product Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/v1/products/` | Retrieve a list of products |
| POST | `/api/v1/products/` | Create a product |
| GET | `/api/v1/products/{id}/` | Retrieve one product |
| PUT | `/api/v1/products/{id}/` | Update a product |
| PATCH | `/api/v1/products/{id}/` | Partially update a product |
| DELETE | `/api/v1/products/{id}/` | Delete a product |

Replace `{id}` with an actual product ID, such as `5`.

## 4. Create a Product

**Method:** `POST`

**Endpoint:**

```text
/api/v1/products/
```

**Headers:**

```http
Content-Type: application/json
```

**Request body:**

```json
{
  "name": "Laptop",
  "description": "A portable computer",
  "price": "55000.00",
  "stock": 10
}
```

A successful creation typically returns `201 Created` with the created product data.

## 5. Retrieve Products

### Retrieve all products

**Method:** `GET`

```text
/api/v1/products/
```

The response contains product data and pagination metadata.

### Retrieve one product

**Method:** `GET`

```text
/api/v1/products/5/
```

Returns the product with ID `5`, if it exists.

If the product does not exist, the API returns an appropriate not-found error.

## 6. Update a Product

### Full update — PUT

**Method:** `PUT`

```text
/api/v1/products/5/
```

Example request body:

```json
{
  "name": "Gaming Laptop",
  "description": "Laptop for gaming",
  "price": "65000.00",
  "stock": 8
}
```

PUT is used for a full update. Include all required fields.

### Partial update — PATCH

**Method:** `PATCH`

```text
/api/v1/products/5/
```

Example request body:

```json
{
  "price": "62000.00"
}
```

PATCH updates only the supplied fields, leaving other fields unchanged.

## 7. Delete a Product

**Method:** `DELETE`

```text
/api/v1/products/5/
```

Deletes the product with ID `5`, if it exists.

A successful deletion commonly returns `204 No Content` when implemented with that response status.

## 8. Query Parameters

Query parameters allow clients to filter, search, and paginate product results without changing the endpoint.

### Filter by minimum price

```text
/api/v1/products/?min_price=100
```

Returns products whose prices are at least `100`.

### Filter by maximum price

```text
/api/v1/products/?max_price=1000
```

Returns products whose prices are at most `1000`.

### Combine price filters

```text
/api/v1/products/?min_price=100&max_price=1000
```

Returns products within the specified price range.

### Search products

```text
/api/v1/products/?search=laptop
```

Searches product names and descriptions for a matching term.

### Paginate results

```text
/api/v1/products/?page=1&page_size=10
```

- `page`: Page number to retrieve.
- `page_size`: Maximum number of products requested per page; the API caps it at `100`.

### Combine filters, search, and pagination

```text
/api/v1/products/?search=laptop&min_price=100&page=1&page_size=10
```

The API applies the supplied filters and search criteria before returning the requested page.

## 9. Pagination Response

A collection response includes pagination information alongside the product data.

Example structure:

```json
{
  "status": "success",
  "count": 25,
  "page": 1,
  "page_size": 10,
  "total_pages": 3,
  "next_page": 2,
  "previous_page": null,
  "data": [
    {
      "id": 5,
      "name": "Laptop",
      "description": "A portable computer",
      "price": "55000.00",
      "stock": 10
    }
  ]
}
```

This is an illustrative example. Actual values depend on the database and request.

- `count`: Total matching products before pagination.
- `page`: Current page number.
- `page_size`: Requested page size after applying the configured limit.
- `total_pages`: Number of available pages.
- `next_page`: Next page number, or `null` if there is no next page.
- `previous_page`: Previous page number, or `null` if there is no previous page.
- `data`: Products on the current page.

## 10. Common HTTP Status Codes

| Status | Meaning |
|---|---|
| `200 OK` | Request completed successfully |
| `201 Created` | Product created successfully |
| `204 No Content` | Successful operation with no response body |
| `400 Bad Request` | Invalid input or query parameters |
| `404 Not Found` | Product does not exist |
| `405 Method Not Allowed` | HTTP method is not supported for the endpoint |
| `500 Internal Server Error` | Unexpected server-side error |

The exact response depends on the operation and the implemented view or exception handler.

## 11. Testing with Postman

1. Start the Django development server.
2. Open Postman and create a request.
3. Select the required HTTP method.
4. Enter the endpoint URL.
5. For POST, PUT, or PATCH, choose **Body → raw → JSON** and enter the request body.
6. Send the request.
7. Verify the status code, response body, and database changes where applicable.

Example local base URL:

```text
http://127.0.0.1:8000
```

Full example:

```text
http://127.0.0.1:8000/api/v1/products/
```

## 12. Important Notes

- Use valid product IDs when testing detail endpoints.
- Send JSON for create and update operations.
- Use positive page numbers and valid page sizes.
- Invalid price filters and invalid price ranges should return validation errors.
- Do not expose `.env` credentials or other secrets in requests, screenshots, or public documentation.
- Example responses are illustrative; verify actual response fields and status codes against the running application.

## 13. Summary

This reference documents the product CRUD endpoints, filtering, searching, pagination, and basic Postman workflow. It provides a consistent starting point for testing and understanding the API.
