from enum import Enum

from django.db import models

from common.models.bases import UuidIdModel
from common.models.utils import enum_as_choices


class BoxTypes(Enum):
    CUSTOM = "custom"  # Box contents are selected by the user
    STATIC = "static"  # Box contents are always the same
    ASSORTED = "assorted"  # Box contents are chosen by ButcherBox staff


class BoxType(UuidIdModel):
    """
    Define a method for how meat should be included in a box.

    A BoxType should provide information both to the user, and to operations as to how
    a box will be comprised of products. For example, an "All Beef" box of type="Static"
    might always have the same cuts, whereas one of type="Assorted" would have different
    cuts every month.
    """

    name = models.CharField(
        max_length=63,
        help_text='User-readable classification of this box type, e.g. "All Beef"',
    )
    description = models.CharField(
        max_length=511, help_text="User-readable description of this box type."
    )
    # type is a reserved word in Python, so we use the trailing underscore convention
    # to namespace it properly and specify the database column name manually.
    _type = models.CharField(
        max_length=63,
        choices=enum_as_choices(BoxTypes),
        db_column="type",
        help_text=(
            "Specifies how box items will be included in this box type. Will they be "
            "chosen by the user? Are they always the same?"
        ),
    )

    def __str__(self):
        return f"{self.name} - {self.description[:40]} ({str(self._type).capitalize()})"
