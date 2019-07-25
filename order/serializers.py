from rest_framework import serializers
from order.models import Order, Payment


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('creator','created_at', 'price', 'order', 'tid', 'status')


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'aid', 'payment_method_type', 'amount', 'item_code', 'created_at', 'tid')