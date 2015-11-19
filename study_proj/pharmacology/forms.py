from django.forms import ModelForm
from pharmacology.models import Drug


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['name','spectrum','clinical_uses','side_effects','notes']
