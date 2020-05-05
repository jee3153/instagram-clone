from django.db import models
from core import models as core_models


class Photo(core_models.TimeStampedModel):

    image = models.ImageField(upload_to="user_postings")
    content = models.TextField(blank=True, null=True)
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="photo"
    )
    likes = models.PositiveIntegerField(default=0)
    is_liked = models.BooleanField(default=False)
    tagged = models.ManyToManyField("accounts.User", related_name="tagged", blank=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ["-created"]
