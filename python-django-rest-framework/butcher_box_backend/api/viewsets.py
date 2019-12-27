from django.contrib.auth import get_user_model
from rest_framework import viewsets

from customer.models import Customer
from box.models import Box, BoxType, BoxItem
from product.models import Product
from subscription.models import Subscription

from .serializers import (
    BoxItemSerializer,
    BoxSerializer,
    BoxTypeSerializer,
    CustomerSerializer,
    ProductSerializer,
    SubscriptionSerializer,
    UserSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class BoxViewSet(viewsets.ModelViewSet):
    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxTypeViewSet(viewsets.ModelViewSet):
    queryset = BoxType.objects.all()
    serializer_class = BoxTypeSerializer


class BoxItemViewSet(viewsets.ModelViewSet):
    serializer_class = BoxItemSerializer

    def get_queryset(self):
        return BoxItem.objects.filter(box=self.kwargs["box_pk"])


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
