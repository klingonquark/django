from django import forms 
from .models import Event


class EmailForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField()


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = "__all__"  # alle Felder, die im Model definiert sind
        # fields = ("name", "author")