from django.urls import include, path
from rest_framework_nested import routers

from . import viewsets


ROUTER = routers.DefaultRouter()
ROUTER.register(r"customers", viewsets.CustomerViewSet)
ROUTER.register(r"boxes", viewsets.BoxViewSet)
ROUTER.register(r"box-types", viewsets.BoxTypeViewSet)
ROUTER.register(r"products", viewsets.ProductViewSet)
ROUTER.register(r"subscriptions", viewsets.SubscriptionViewSet)
ROUTER.register(r"users", viewsets.UserViewSet)

BOX_ITEMS_ROUTER = routers.NestedSimpleRouter(ROUTER, r"boxes", lookup="box")
BOX_ITEMS_ROUTER.register(r"items", viewsets.BoxItemViewSet, basename="items")


urlpatterns = [
    path("", include(ROUTER.urls)),
    path("", include(BOX_ITEMS_ROUTER.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
