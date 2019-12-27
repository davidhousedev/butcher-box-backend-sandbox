from django.db import models

from common.models.bases import UuidIdModel


class Product(UuidIdModel):
    """
    Describes a product which can be included in a box.

    Products should be derived from a CMS content source and synced between data sources
    through the use of an internal UID. The only role capable of updating this data
    should be the CMS, enforced by strict authorization protocols.

    If these entities are edited by-hand in Django, it introduces a discrepancy between
    the canonical data source in the CMS and the derived data source here in Django.
    """

    name = models.CharField(max_length=63)
    description = models.TextField(max_length=511)
    weight_g = models.IntegerField()
    size_cubic_cm = models.IntegerField()
