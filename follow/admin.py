from django.contrib import admin
from . import models


@admin.register(models.FollowRelationship)
class FollowerAdmin(admin.ModelAdmin):
    list_display = ("follower",)
