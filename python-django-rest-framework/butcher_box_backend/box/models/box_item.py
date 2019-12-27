from enum import Enum

from django.db import models

from common.models.bases import UuidIdModel
from common.models.utils import enum_as_choices


class BoxItemTypes(Enum):
    SUBSCRIPTION = "subscription"
    PROMOTION = "promotion"
    OFFER = "offer"
    ADDON = "addon"


class BoxItem(UuidIdModel):
    """
    Define how a specific product is included within a box.

    This model is concerned with how a box is populated with items. For example,
    some boxes may be comprised of items which are part of a subscription, on-demand
    addons, free promos, etc.
    """

    box = models.ForeignKey("Box", on_delete=models.CASCADE, related_name="box_items")
    # If a Product is deleted, this could create some strange information in users'
    # order histories. If a Product absolutely must be deleted, then all instances of
    # that BoxItem should be set to a different Product first, before the deletion
    # should proceed. Alternatively, all BoxItems of that type could be archived to a
    # different datastore and deleted from this database, then the Product could be
    # safely deleted. Guard against this using models.PROTECT, which maps to SQL
    # RESTRICT.
    # cf: https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.PROTECT
    product = models.ForeignKey("product.Product", on_delete=models.PROTECT)
    # type is a reserved word in Python, so we use the trailing underscore convention
    # to namespace it properly and specify the database column name manually.
    _type = models.CharField(
        max_length=63,
        choices=enum_as_choices(BoxItemTypes),
        default=BoxItemTypes.SUBSCRIPTION.name,
        db_column="type",
    )
