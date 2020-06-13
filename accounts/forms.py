from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


class EditProfileForm(forms.ModelForm):
    profile = forms.ImageField(
        required=False,
        error_messages={"invald": ("Image files only.")},
        widget=forms.FileInput,
    )

    class Meta:
        model = User
        fields = ("first_name", "username", "email", "profile", "bio")


class SearchForm(forms.Form):
    username = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={"placeholder": "Search by username"}),
    )

    class Meta:
        model = User
        fields = ("username",)
