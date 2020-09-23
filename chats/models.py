from django.db import models
from core import models as core_models


class Chat(core_models.TimeStampedModel):
    """ Chat Model Definition """

    participants = models.ManyToManyField(
        "accounts.User", related_name="chat", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ",".join(usernames)

    # def chattingwith(self):
    #     return self.participants[0]

    def count_messages(self):
        return self.messages.count()

    count_messages.short_description = "Number of Messages"

    def count_participants(self):
        return self.participants.count()

    count_participants.short_description = "Number of Participants"


class Message(core_models.TimeStampedModel):
    """ Message Model Definition """

    message = models.TextField(default="")
    user = models.ForeignKey(
        "accounts.User", related_name="messages", on_delete=models.CASCADE
    )
    chat = models.ForeignKey("Chat", related_name="messages", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user}: {self.message}"
