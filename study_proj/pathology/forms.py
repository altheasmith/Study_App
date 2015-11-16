from django.forms import ModelForm
from pathology.models import Disease


class DiseaseForm(ModelForm):
    class Meta:
        model = Disease
        fields = ['name','clinical_presentation','treatment','notes']
