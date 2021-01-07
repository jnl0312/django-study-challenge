from django.contrib import admin
from . import models


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "year",
        "category",
        "cover_image",
        "rating",
        "writer",
    )

    list_filter = (
        "year",
        "category",
        "rating",
        "writer",

    )
