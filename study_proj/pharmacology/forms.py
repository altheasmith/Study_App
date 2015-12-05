from django.forms import ModelForm
from pharmacology.models import Drug


class DrugForm(ModelForm):
    class Meta:
        model = Drug
        fields = ['class_name','name','mechanism','clinical_uses','side_effects','contraindications','notes']
