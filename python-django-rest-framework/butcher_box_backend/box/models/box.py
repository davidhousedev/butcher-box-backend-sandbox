from django.db import models

from common.models.bases import UuidIdModel


class Box(UuidIdModel):
    """
    Define a specific instance of a box which will be shipped.

    Boxes are comprised of items and a type. Attributes pertain to
    logistics of shipping that specific box.
    """

    shipped = models.DateTimeField(
        null=True,
        default=None,
        help_text="The date and time that this box was shipped.",
    )
    delivered = models.DateTimeField(
        null=True,
        default=None,
        help_text="The date and time this box was reported delivered.",
    )
    # Protect deletion of Boxes when BoxTypes and Customers are deleted, in order to
    # preserve the integrity of order history.
    _type = models.ForeignKey(
        "BoxType",
        on_delete=models.PROTECT,
        db_column="type",
        help_text="The abstract description of this box.",
    )
    customer = models.ForeignKey(
        "customer.Customer",
        on_delete=models.PROTECT,
        help_text="Who was billed for this box.",
    )

    def __str__(self):
        return f"{self._type.name} box for {self.customer} [{self.uid}]"
