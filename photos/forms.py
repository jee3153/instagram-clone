from django import forms
from . import models
from accounts.models import User


class PostForm(forms.ModelForm):
    image = forms.ImageField(
        required=True,
        error_messages={"invalid": ("Image files only.")},
        widget=forms.FileInput,
    )

    class Meta:
        model = models.Photo
        fields = ("image", "content")
        widgets = {
            "content": forms.TextInput(attrs={"placeholder": "Write a caption..."}),
        }


class SearchForm(forms.Form):
    content = forms.CharField(
        required=False, widget=forms.TextInput(attrs={"placeholder": "Search by post"})
    )

    class Meta:
        model = models.Photo
        fields = ("content",)
