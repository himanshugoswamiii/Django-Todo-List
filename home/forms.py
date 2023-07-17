from django import forms

class AddEntryForm(forms.Form):
    id = forms.IntegerField()
    itemName = forms.CharField(max_length=100)
    complete = forms.BooleanField(required=False)
