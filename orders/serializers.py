from rest_framework import serializers
from .models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["id", "status", "created_at", "seller_id", "products", "user"]
        read_only_fields = ["id", "created_at"]