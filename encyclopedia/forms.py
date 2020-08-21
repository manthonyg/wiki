from django import forms

class NewEntryForm(forms.Form):
    title = forms.CharField(required=True)
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={"rows":3, "cols":20}))