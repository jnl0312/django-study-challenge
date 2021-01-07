from django.db import models
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
    title = models.CharField(max_length=50)
    year = models.DateField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.SET_NULL, null=True)
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField()
    writer = models.ForeignKey(
        "people.Person", on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.title
