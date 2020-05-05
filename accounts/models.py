from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    LOGIN_EMAIL = "email"
    LOGIN_FACEBOOK = "facebook"

    LOGIN_CHOICES = ((LOGIN_EMAIL, "Email"), (LOGIN_FACEBOOK, "Facebook"))

    login_method = models.CharField(
        max_length=30, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    bio = models.TextField(max_length=300, blank=True)
    profile = models.ImageField(upload_to="user_profiles/%Y/%m/%d", blank=True)
    followers = models.ManyToManyField("self", related_name="+", symmetrical=False)
    followings = models.ManyToManyField("self", related_name="+", symmetrical=False)
    followed = models.BooleanField(default=False)
