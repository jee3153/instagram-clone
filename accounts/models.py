from django.db import models
from django.contrib.auth.models import AbstractUser
from core import managers as core_managers


class User(AbstractUser):

    LOGIN_EMAIL = "email"
    LOGIN_FACEBOOK = "facebook"

    LOGIN_CHOICES = ((LOGIN_EMAIL, "Email"), (LOGIN_FACEBOOK, "Facebook"))

    FEMALE = "female"
    MALE = "male"
    NOT_SPECIFIED = "not specified"

    GENDER_CHOICES = (
        (FEMALE, "Female"),
        (MALE, "Male"),
        (NOT_SPECIFIED, "Prefer not specified"),
    )

    login_method = models.CharField(
        max_length=30, choices=LOGIN_CHOICES, default=LOGIN_EMAIL
    )
    bio = models.TextField(max_length=300, blank=True)
    profile = models.ImageField(upload_to="user_profiles/", null=True, blank=True)
    gender = models.CharField(
        max_length=40, choices=GENDER_CHOICES, default=NOT_SPECIFIED, null=True
    )
    objects = core_managers.CustomUserManager()

    def __str__(self):
        return self.username
