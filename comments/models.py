from django.db import models
from django.shortcuts import reverse
from core import models as core_models


class Comment(core_models.TimeStampedModel):
    commenter = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="comment"
    )
    comment = models.TextField(blank=True, null=True, editable=True)
    photo = models.ForeignKey(
        "photos.Photo", on_delete=models.CASCADE, related_name="comment"
    )
    mention = models.ManyToManyField(
        "accounts.User", related_name="mention", blank=True
    )
    like = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.comment

    def get_absolute_url(self):
        return reverse("comments:list", kwargs={"photo_pk": self.photo_id})

    class Meta:
        ordering = ["-created"]
