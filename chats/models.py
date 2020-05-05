from django.db import models
from core import models as core_models


class Chat(core_models.TimeStampedModel):
    participants = models.ManyToManyField(
        "accounts.User", related_name="chat", blank=True
    )


class Message(core_models.TimeStampedModel):
    user = models.ForeignKey(
        "accounts.User", related_name="message", on_delete=models.CASCADE
    )
    chat = models.ForeignKey("Chat", on_delete=models.CASCADE)
