from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):
    list_display = (
        "created_by",
        "show_books",
        "show_movies",
    )

    list_filter = (
        "created_by",
        "books",
        "movies",
    )

    def show_books(self, obj):
        return obj.books.all().first()

    def show_movies(self, obj):
        return obj.movies.all().first()
