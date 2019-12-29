from django.db import models
from django.contrib.auth import get_user_model

from common.models.bases import UuidIdModel


class Customer(UuidIdModel):
    # TODO: Implement address storage in a way that can be keyed off of the User,
    #       so that it can be deleted when user data deletion requests are made.
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        default=None,
        help_text=(
            "Relationship to the internal application user. This model is separate "
            "from the internal user in order to ensure that user data can be isolated "
            "from subscription data, for e.g. managing CCPA requirements."
        ),
    )

    def __str__(self):
        return f"{self.user} [{self.uid}]"
