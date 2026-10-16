
from decimal import Decimal, InvalidOperation

from django.core.paginator import Paginator, InvalidPage
from django.db.models import Q

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializer


# Standard error response used by our API views.
def error_response(message, errors=None, http_status=400):
    body = {
        "status": "error",
        "message": message,
    }

    # Include field-level errors when validation fails.
    if errors is not None:
        body["errors"] = errors

    return Response(body, status=http_status)


# GET: Check whether the API is running.
@api_view(["GET"])
def health_check(request):
    return Response(
        {
            "status": "success",
            "message": "REST API is running",
        },
        status=status.HTTP_200_OK,
    )


# GET: Retrieve products with filtering, search and pagination.
# POST: Create a new product.
@api_view(["GET", "POST"])
def product_list_create(request):

    # Handle GET requests.
    if request.method == "GET":

        # Step 1: Start with all products.
        products = Product.objects.all()

        # Step 2: Read optional filtering and search parameters.
        min_price_raw = request.query_params.get(
            "min_price", ""
        ).strip()

        max_price_raw = request.query_params.get(
            "max_price", ""
        ).strip()

        search = request.query_params.get(
            "search", ""
        ).strip()

        errors = {}

        # Convert and validate a price query parameter.
        def parse_price_param(name, raw_value):
            if not raw_value:
                return None

            try:
                value = Decimal(raw_value)
            except (InvalidOperation, ValueError):
                errors[name] = ["Enter a valid number."]
                return None

            # Reject negative and non-finite prices.
            if not value.is_finite() or value < 0:
                errors[name] = [
                    "Enter a valid non-negative price."
                ]
                return None

            return value

        # Validate minimum and maximum prices.
        min_price = parse_price_param(
            "min_price", min_price_raw
        )

        max_price = parse_price_param(
            "max_price", max_price_raw
        )

        # Ensure the minimum does not exceed the maximum.
        if (
            min_price is not None
            and max_price is not None
            and min_price > max_price
        ):
            errors["price_range"] = [
                "min_price cannot be greater than max_price."
            ]

        # Return an error if price parameters are invalid.
        if errors:
            return error_response(
                "Invalid query parameters.",
                errors=errors,
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Step 3: Apply the minimum price filter.
        if min_price is not None:
            products = products.filter(
                price__gte=min_price
            )

        # Step 4: Apply the maximum price filter.
        if max_price is not None:
            products = products.filter(
                price__lte=max_price
            )

        # Step 5: Search names and descriptions.
        if search:
            products = products.filter(
                Q(name__icontains=search)
                | Q(description__icontains=search)
            )

        # Step 6: Read pagination parameters.
        page_raw = request.query_params.get("page", "1").strip()
        page_size_raw = request.query_params.get(
            "page_size", "10"
        ).strip()

        # Convert page and page_size into integers.
        try:
            page_number = int(page_raw)
            page_size = int(page_size_raw)
        except ValueError:
            return error_response(
                "Invalid pagination parameters.",
                errors={
                    "page": [
                        "page and page_size must be integers."
                    ]
                },
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Page numbers and page sizes must be positive.
        if page_number < 1 or page_size < 1:
            return error_response(
                "Invalid pagination parameters.",
                errors={
                    "page": [
                        "page and page_size must be positive integers."
                    ]
                },
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Limit page size to prevent excessively large responses.
        if page_size > 100:
            return error_response(
                "Invalid pagination parameters.",
                errors={
                    "page_size": [
                        "page_size cannot exceed 100."
                    ]
                },
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Step 7: Create a paginator for the filtered products.
        paginator = Paginator(products, page_size)

        # Select the requested page.
        try:
            page_obj = paginator.page(page_number)
        except InvalidPage:
            return error_response(
                "Invalid page number.",
                errors={
                    "page": [
                        "The requested page does not exist."
                    ]
                },
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        # Step 8: Serialize only the products on this page.
        serializer = ProductSerializer(
            page_obj.object_list,
            many=True,
        )

        # Return pagination metadata and the current page's data.
        return Response(
            {
                "status": "success",
                "count": paginator.count,
                "page": page_number,
                "page_size": page_size,
                "total_pages": paginator.num_pages,
                "next_page": (
                    page_number + 1
                    if page_obj.has_next()
                    else None
                ),
                "previous_page": (
                    page_number - 1
                    if page_obj.has_previous()
                    else None
                ),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # Handle POST requests: create a product.
    serializer = ProductSerializer(data=request.data)

    if not serializer.is_valid():
        return error_response(
            "Validation failed.",
            errors=serializer.errors,
            http_status=status.HTTP_400_BAD_REQUEST,
        )

    # Save the validated product through the Django ORM.
    product = serializer.save()

    return Response(
        {
            "status": "success",
            "message": "Product created successfully.",
            "data": ProductSerializer(product).data,
        },
        status=status.HTTP_201_CREATED,
    )


# GET: Retrieve one product.
# PUT: Replace editable product data.
# PATCH: Update selected fields.
# DELETE: Delete one product.
@api_view(["GET", "PUT", "PATCH", "DELETE"])
def product_detail(request, pk):

    # Find the product using the path parameter.
    product = Product.objects.filter(pk=pk).first()

    # Return 404 if the product does not exist.
    if product is None:
        return error_response(
            "Product not found.",
            http_status=status.HTTP_404_NOT_FOUND,
        )

    # GET: Retrieve one product.
    if request.method == "GET":
        serializer = ProductSerializer(product)

        return Response(
            {
                "status": "success",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK,
        )

    # PUT and PATCH: Update an existing product.
    if request.method in ["PUT", "PATCH"]:
        partial_update = request.method == "PATCH"

        serializer = ProductSerializer(
            product,
            data=request.data,
            partial=partial_update,
        )

        if not serializer.is_valid():
            return error_response(
                "Validation failed.",
                errors=serializer.errors,
                http_status=status.HTTP_400_BAD_REQUEST,
            )

        updated_product = serializer.save()

        return Response(
            {
                "status": "success",
                "message": "Product updated successfully.",
                "data": ProductSerializer(updated_product).data,
            },
            status=status.HTTP_200_OK,
        )

    # DELETE: Remove the product.
    product.delete()

    # HTTP 204 means successful deletion with no response body.
    return Response(status=status.HTTP_204_NO_CONTENT)
