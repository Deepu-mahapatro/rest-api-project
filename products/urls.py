
from django.urls import path

from .views import (
    health_check,
    product_list_create,
    product_detail,
)

urlpatterns = [
    # API health check.
    path("health/", health_check, name="health-check"),

    # Collection endpoint:
    # GET lists/filter/search products; POST creates a product.
    path(
        "products/",
        product_list_create,
        name="product-list-create",
    ),

    # Path parameter: <int:pk> captures the product ID.
    # GET, PUT, PATCH and DELETE operate on that product.
    path(
        "products/<int:pk>/",
        product_detail,
        name="product-detail",
    ),
]
