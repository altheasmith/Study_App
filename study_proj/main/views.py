from django.shortcuts import render
from django.views.generic import View
from microbiology.models import Bacterium, Virus, Fungus, Parasite
from pathology.models import Disease
from pharmacology.models import Drug
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from microbiology.forms import BacteriumForm, VirusForm, FungusForm, ParasiteForm
from pathology.forms import DiseaseForm
from pharmacology.forms import DrugForm


class MainView(View):
    def get(self, request):
        bacterium = Bacterium.objects.get(id=1)
        context = {
                'bacterium':bacterium,
                'bac_form':BacteriumForm(),
                'vir_form':VirusForm().as_table(),
                'fun_form':FungusForm().as_table(),
                'par_form':ParasiteForm().as_table(),
                'dis_form':DiseaseForm().as_table(),
                'dru_form':DrugForm().as_table(),
        }
        return render(request,'main/index.html', context)

class AddView(View):
    def get(self, request, card_type):
        print(card_type)
        card_type_dict = {
            'bac':BacteriumForm().as_p(),
            'vir':VirusForm().as_p(),
            'fun':FungusForm().as_p(),
            'par':ParasiteForm().as_p(),
            'dis':DiseaseForm().as_p(),
            'dru':DrugForm().as_p()
            }
        form = card_type_dict[card_type]
        print(form)
        return JsonResponse({'form':form})
