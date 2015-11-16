from django.forms import ModelForm
from pharmacology.models import Drug


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['name','use','side_effects','notes']
