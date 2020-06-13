from django.db import models
from core import models as core_models
from django.shortcuts import reverse


class Photo(core_models.TimeStampedModel):

    image = models.ImageField(upload_to="user_postings")
    content = models.TextField(blank=True, null=True, default="")
    author = models.ForeignKey(
        "accounts.User", on_delete=models.CASCADE, related_name="photo"
    )
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse("photos:detail", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-created"]


class Likes(models.Model):
    photo = models.OneToOneField(Photo, related_name="post", on_delete=models.CASCADE)
    likers = models.ManyToManyField("accounts.User", related_name="likers")
