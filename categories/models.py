from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- Category
  name
  kind (book/movie/both)
"""


class Category(core_models.TimeStampedModel):
    """ Category Model Definition """
    KIND_BOOK = "book"
    KIND_MOVIE = "movie"
    KIND_BOTH = "both"

    KIND_CHOICES = (
        (KIND_BOOK, "Book"),
        (KIND_MOVIE, "Movie"),
        (KIND_BOTH, "Both"),
    )

    name = models.CharField(max_length=80)
    kind = models.CharField(
        max_length=10, choices=KIND_CHOICES, default=KIND_BOTH)

    # book이나 movie를 추가할 때 category 이름들을 확인할 수 있음.
    def __str__(self):
        return self.name
