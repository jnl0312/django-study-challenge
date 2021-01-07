from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (ManyToMany => categories.Category)
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""


class Movie(core_models.TimeStampedModel):
    """ Movie Model Definition """
    title = models.CharField(max_length=50)
    year = models.DateField()
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField()
    category = models.ManyToManyField(
        "categories.Category", blank=True)
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="kind_director")
    cast = models.ManyToManyField(
        "people.Person", blank=True, related_name="kind_cast")

    def __str__(self):
        return self.title
