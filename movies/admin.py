from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "rating",
        #    "cover_image",
        #    "director",
        #    "show_categories",

    )

    list_filter = (
        #    "title",
        "year",
        "rating",
        #    "cover_image",
        #    "director",
        #    "category",
    )


"""
    def show_categories(self, obj):
        return obj.category.all().first()
"""
