from django import forms

class SearchForm(forms.Form):
    coords = forms.CharField(max_length=255)

