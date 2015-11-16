from django.forms import ModelForm
from microbiology.models import Bacterium, Virus, Fungus, Parasite


class BacteriumForm(ModelForm):
    class Meta:
        model = Bacterium
        fields = ['genus','species','shape','aerobic','clinical_presentation','treatment','notes']


class VirusForm(ModelForm):
    class Meta:
        model = Virus
        fields = ['name','clinical_presentation','treatment','notes']


class FungusForm(ModelForm):
    class Meta:
        model = Fungus
        fields = ['name','clinical_presentation','treatment','notes']


class ParasiteForm(ModelForm):
    class Meta:
        model = Parasite
        fields = ['name','clinical_presentation','treatment','notes']
