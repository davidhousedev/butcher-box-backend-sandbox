from enum import Enum

from django.db import models

from common.models.utils import enum_as_choices
from common.models.bases import UuidIdModel


class BillFrequencyEnum(Enum):
    MONTH = "month"
    DAY = "day"
    WEEK = "week"


class Subscription(UuidIdModel):  # pylint: disable=too-few-public-methods
    bill_date = models.DateField(
        null=True,
        default=None,
        help_text=(
            "Calendar date when this subscription should be billed. If `None`, "
            "it is considered inactive."
        ),
    )
    bill_frequency = models.CharField(
        max_length=31,
        choices=enum_as_choices(BillFrequencyEnum),
        default=BillFrequencyEnum.MONTH.name,
        help_text="How the bill_interval be measured",
    )
    bill_interval = models.IntegerField(
        default=1,
        help_text=(
            "How many e.g. days, weeks, months until this subscription should be billed"
        ),
    )
    customer = models.ForeignKey(
        "customer.Customer",
        on_delete=models.CASCADE,
        help_text="The person who should be billed for this subscription",
    )
    # In the event that a box type is deleted, all Subscriptions should be migrated
    # to a different BoxType beforehand. Ensure that a BoxType cannot be deleted
    # in a way that prevents a subscription from having a specified BoxType.
    box_type_preference = models.ForeignKey(
        "box.BoxType",
        on_delete=models.PROTECT,
        help_text="The abstract type of box which should be delivered every interval.",
    )
    next_box = models.ForeignKey(
        "box.Box",
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        help_text="The instance of the next box to be delivered to this subscription.",
    )

    def __str__(self):
        return (
            f'{self.customer}\'s {"active" if self.bill_date else "inactive"} '
            "subscription for {self.box_type_preference}"
        )
