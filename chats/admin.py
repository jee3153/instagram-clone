from django.contrib import admin
from . import models


@admin.register(models.Chat)
class ChatAdmin(admin.ModelAdmin):
    # list_display = ("id", "chat")
    pass


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    pass
