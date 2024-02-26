from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['event_name', 'event_place', 'event_date', 'event_description', 'event_coordinator']
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'})
        }