from django.contrib.auth import get_user_model
from rest_framework import serializers

from customer.models import Customer
from box.models import Box, BoxType, BoxItem
from product.models import Product
from subscription.models import Subscription


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        exclude = ["id", "password"]


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Customer
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["uid", "name", "description", "weight_g", "size_cubic_cm", "url"]


class BoxItemSerializer(serializers.ModelSerializer):
    box = serializers.SlugRelatedField(queryset=Box.objects, slug_field="uid")

    class Meta:
        model = BoxItem
        fields = "__all__"
        read_only_fields = ["box"]


class BoxItemListSerializer(BoxItemSerializer):
    box = None

    class Meta:
        model = BoxItem
        exclude = ["box"]
        depth = 2


class BoxTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoxType
        fields = ["uid", "name", "description", "_type", "url"]


class BoxSerializer(serializers.ModelSerializer):
    box_items = BoxItemListSerializer(many=True, default=[])

    def create(self, validated_data):
        """
        Override to allow for creation of box_items from the box browsable API

        cf: https://www.django-rest-framework.org/api-guide/relations/#writable-nested-serializers
        """
        box_item_data = validated_data.pop("box_items")

        box = super().create(validated_data)

        for box_item in box_item_data:
            BoxItem.objects.create(box=box, **box_item)
        return box

    def update(self, instance, validated_data):
        """
        Override to allow for modification of box_items from the box browsable API

        Note: This method does not allow for implicit deletions of box items. In order
              to remove a box item, you have to DELETE the item by id.
        """
        box_item_data = validated_data.pop("box_items")

        instance = super().update(instance, validated_data)

        for item in box_item_data:
            instance.box_items.update_or_create(**item)
        return instance

    class Meta:
        model = Box
        fields = [
            "uid",
            "box_items",
            "_type",
            "shipped",
            "delivered",
            "customer",
            "url",
        ]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = [
            "uid",
            "bill_date",
            "bill_frequency",
            "bill_interval",
            "customer",
            "box_type_preference",
            "next_box",
        ]
