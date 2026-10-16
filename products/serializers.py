
from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product

        # Fields exposed through the API.
        fields = [
            "id",
            "name",
            "description",
            "price",
            "stock",
            "created_at",
            "updated_at",
        ]

        # Clients cannot set these fields directly.
        read_only_fields = ["id", "created_at", "updated_at"]

    # Validate the price before saving a product.
    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Price cannot be negative."
            )

        return value
