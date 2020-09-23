from django import forms


class sendMessage(forms.Form):

    message = forms.CharField(
        required=True, widget=forms.TextInput(attrs={"placeholder": "send a message"})
    )
