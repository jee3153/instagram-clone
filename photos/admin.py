from django.contrib import admin
from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "likes", "is_liked")
    list_display_links = ("author", "content")
