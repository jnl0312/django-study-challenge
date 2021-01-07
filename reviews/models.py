from django.db import models
from core import models as core_models
"""
Here are the models you have to create:
- Review
  created_by (ForeignKey => users.User)
  text
  movie (ForeignKey => movies.Movie, null,blank)
  book (ForeignKey => movies.Movie, null,blank)
  rating
"""


class Review(core_models.TimeStampedModel):
    """ Review Model Definition """
    created_by = models.ForeignKey("users.User", on_delete=models.CASCADE)
    text = models.TextField()
    movie = models.ForeignKey(
        "movies.Movie", on_delete=models.CASCADE, null=True, blank=True)
    book = models.ForeignKey(
        "books.book", on_delete=models.CASCADE, null=True, blank=True)
    rating = models.IntegerField()
