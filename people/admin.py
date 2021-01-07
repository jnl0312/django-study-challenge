from django.contrib import admin

from . import models
# Register your models here.


@admin.register(models.Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "photo",
        "kind",
    )

    list_filter = (
        "name",
        "kind",
    )
