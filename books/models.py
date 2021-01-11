from django.db import models
from django.db.models.fields import related
from core import models as core_models
"""
Here are the models you have to create:
- Book:
  title
  year
  category (ForeignKey => categories.Category)
  cover_image
  rating
  writer (ForeignKey => people.Person)
"""


class Book(core_models.TimeStampedModel):

    """ Book Model Definition """
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, null=True, related_name="books")
    cover_image = models.ImageField(blank=True)
    rating = models.FloatField()
    writer = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, blank=True, null=True, related_name="books")

    def __str__(self):
        return self.title
