from django import forms

from .models import Registration, Contests


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'registration_date': forms.DateInput(format='%d/%m/%Y', attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['contest'].queryset = Contests.objects.none()

        if 'event' in self.data:
            try:
                event_id = self.data.get('event')
                self.fields['contest'].queryset = Contests.objects.filter(event=event_id).order_by('contest_name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['contest'].queryset = self.instance.event.contests.order_by('contest_name')


