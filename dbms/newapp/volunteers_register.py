from django import forms
from .models import Volunteers,Department,Events


class VolunteersForm(forms.ModelForm):
    '''department = forms.ModelChoiceField(
        queryset=Department.objects.all(),  # Query to retrieve all driver records
        widget=forms.Select,
        label="Department",
        required=True
    )

    events = forms.ModelChoiceField(
        queryset=Events.objects.all(),  # Query to retrieve all vehicle records
        widget=forms.Select,
        label="Events",
        required=True
    )'''
    class Meta:
        model = Volunteers
        fields = ['volunteer_id', 'volunteer_roll_no', 'volunteer_name', 'volunteer_age', 'volunteer_contact', 'volunteer_email','dept','eid']

