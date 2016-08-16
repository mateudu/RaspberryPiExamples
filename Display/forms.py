from django import forms


class DisplayPostForm(forms.Form):
    first_line = forms.CharField(required=False)
    second_line = forms.CharField(required=False)