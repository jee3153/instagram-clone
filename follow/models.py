from django.db import models


class FollowRelationship(models.Model):
    follower = models.OneToOneField(
        "accounts.User", related_name="follower", on_delete=models.CASCADE
    )
    followings = models.ManyToManyField("accounts.User", related_name="followings")
    followed = models.ManyToManyField("accounts.User", related_name="followed")
