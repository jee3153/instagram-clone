from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.TextInput(attrs={"placeholder": "Comment"}))

    class Meta:
        model = Comment
        fields = ("comment",)
