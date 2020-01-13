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
    """
    Create boxes that will be delivered to specific customers.

    Add a new box to deliver a box to a user, or modify box contents to change the items
    that will be delivered in that box. Providers can PATCH to specific boxes to update
    shipment dates, and a user may PATCH to report that they have received a box.
    """

    queryset = Box.objects.all()
    serializer_class = BoxSerializer


class BoxTypeViewSet(viewsets.ModelViewSet):
    """
    Add additional abstract box types which users can purchase or subscribe to.

    Box types specify what type of meat will be included in a box, and how that box
    should be created. Is it a `CUSTOM` box, where the user will select their own meat?
    Is it `ASSORTED`, where operations will select the meat to include? Or is it
    `STATIC`, which will include the same cuts every time?
    """

    queryset = BoxType.objects.all()
    serializer_class = BoxTypeSerializer


class BoxItemViewSet(viewsets.ModelViewSet):
    """
    Add products to a specific box, which will be shipped to a customer.

    Box items can be added to a box with a few different methods. They may be part of a
    subscription, an addon, or a promotion.
    """

    serializer_class = BoxItemSerializer

    def get_queryset(self):
        return BoxItem.objects.filter(box=self.kwargs["box_pk"])


class ProductViewSet(viewsets.ModelViewSet):
    """
    Add a new product which can be shipped in a box.

    The list of products should be a derived from a CMS and should not be modified
    manually.
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SubscriptionViewSet(viewsets.ModelViewSet):
    """
    Create subscriptions of for box delivery, for a specific customer.

    Subscriptions are considered active when bill_date is not null.
    """

    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
