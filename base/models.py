import uuid

from django.db import models

# Create your models here.


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract: True


class GenericBaseModel(BaseModel):
    name = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        abstract: True


class State(GenericBaseModel):
    def __str__(self):
        return self.name
