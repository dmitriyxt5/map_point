from django import forms
from .models import MapPoint


class MapPointForm(forms.ModelForm):
    class Meta:
        model = MapPoint
        fields = [
            'title',
            'description',
            'latitude',
            'longitude',
            'image',
        ]

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название'}),
            'description': forms.Textarea(attrs={'rows': 3}),
        }
