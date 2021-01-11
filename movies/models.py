from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- Movie:
  title
  year
  cover_image
  rating
  category (Foreignkey => categories.Category) : manytomany에서 과제 정답은 바뀜
  director (ForeignKey => people.Person)
  cast (ManyToMany => people.Person)
"""


class Movie(core_models.TimeStampedModel):
    """ Movie Model Definition """
    title = models.CharField(max_length=120)
    year = models.IntegerField()
    cover_image = models.ImageField(blank=True)
    rating = models.IntegerField()
    category = models.ForeignKey(
        "categories.Category", on_delete=models.CASCADE, related_name="movies", null=True)
    director = models.ForeignKey(
        "people.Person", on_delete=models.CASCADE, related_name="movies")
    cast = models.ManyToManyField(
        "people.Person", blank=True)

    def __str__(self):
        return self.title
