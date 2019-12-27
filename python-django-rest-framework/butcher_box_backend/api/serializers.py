from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_nested.relations import NestedHyperlinkedRelatedField

from customer.models import Customer
from box.models import Box, BoxType, BoxItem
from product.models import Product
from subscription.models import Subscription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = "__all__"


class BoxItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxItem
        fields = "__all__"


class BoxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxType
        fields = "__all__"


class BoxSerializer(serializers.ModelSerializer):
    box_items = BoxItemSerializer(many=True, read_only=True)
    _type = BoxTypeSerializer(read_only=True, label="type")

    class Meta:
        model = Box
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = "__all__"
