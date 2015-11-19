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
import random


len_dict = {
            'patho':len(Disease.objects.all()),
            'pharm':len(Drug.objects.all()),
            'bac':len(Bacterium.objects.all()),
            'vir':len(Virus.objects.all()),
            'fun':len(Fungus.objects.all()),
            'par':len(Parasite.objects.all())
            }

object_dict = {
            'patho':Disease,
            'pharm':Drug,
            'bac':Bacterium,
            'vir':Virus,
            'fun':Fungus,
            'par':Parasite
            }

class MainView(View):
    def get(self, request):
        return render(request,'main/index.html')

class GetCard(View):
    def get(self, request, card_type):
        if card_type == 'micro':
            card_type_dict = {1:'bac', 2:'vir', 3:'fun', 4:'par'}
            card_type = card_type_dict[random.randint(1,4)]
        if len_dict[card_type] == 0:
            return JsonResponse({'card':'0'})
        card_id = random.randint(1,len_dict[card_type])
        card = object_dict[card_type].objects.get(id=card_id)
        card_dict = model_to_dict(card)
        if 'aerobic' in card_dict:
            card_dict['aerobic'] = card.get_aerobic_display()
        if 'shape' in card_dict:
            card_dict['shape'] = card.get_shape_display()
        card_dict['type'] = type(card).__name__
        return JsonResponse({'card':card_dict})
