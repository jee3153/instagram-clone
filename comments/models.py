from django.db import models
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
    is_liked = models.BooleanField(default=False)

    def __str__(self):
        return self.comment