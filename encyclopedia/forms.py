from django import forms

class NewEntryForm(forms.Form):
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'pure-input-1', 'placeholder': 'Content'}))
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={'class': 'pure-input-1', 'placeholder': 'Content'}))