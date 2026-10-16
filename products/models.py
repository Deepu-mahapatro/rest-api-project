
from django.db import models


class Product(models.Model):
    # Product name; maximum length is 150 characters.
    name = models.CharField(max_length=150)

    # Description is optional.
    description = models.TextField(blank=True, default="")

    # Price supports up to 10 digits, including 2 decimal places.
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # Stock cannot be negative through normal field validation.
    stock = models.PositiveIntegerField(default=0)

    # Automatically records when the product is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Automatically updates whenever the product is saved.
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        # Return products in ascending ID order by default.
        ordering = ["id"]

        # Database-level protection against negative prices.
        constraints = [
            models.CheckConstraint(
                condition=models.Q(price__gte=0),
                name="product_price_nonnegative",
            ),
        ]

    def __str__(self):
        # Human-readable representation of the product.
        return self.name
