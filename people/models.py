from django.db import models
from django.db.models.enums import Choices
from core import models as core_models
"""
- Person
  name
  kind (choice=Actor/Director/Writer)
  photo
"""


class Person(core_models.TimeStampedModel):
    """ Person Model Definition """
    KIND_ACTOR = "actor"
    KIND_DIRECTOR = "director"
    KIND_WRITER = "writer"
    KIND_CHOICES = (
        (KIND_ACTOR, "actor"),
        (KIND_DIRECTOR, "director"),
        (KIND_WRITER, "writer"),
    )

    name = models.CharField(max_length=30)
    kind = models.CharField(max_length=15, choices=KIND_CHOICES)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return self.name
