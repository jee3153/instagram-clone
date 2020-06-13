from django.contrib import admin
from . import models


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("author", "content", "likes", "created")
    list_display_links = ("author", "content")


@admin.register(models.Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ("photo",)
