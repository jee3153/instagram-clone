from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta:
        model = models.Photo
        fields = ['image', 'content', 'tagged']
