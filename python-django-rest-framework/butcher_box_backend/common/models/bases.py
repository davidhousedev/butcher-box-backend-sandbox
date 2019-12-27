import uuid

from django.db import models


class UuidIdModel(models.Model):
    # Django will automatically create an auto-incrementing int field as
    # a primary key, but we use a uid field as a decoupled, url-safe id
    # for querying
    uid = models.UUIDField(
        unique=True, default=uuid.uuid4, editable=False, primary_key=True
    )

    class Meta:
        abstract = True
