from django.contrib import admin
from . import models


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("photo", "commenter", "comment")
    list_display_links = ("photo", "commenter", "comment")
