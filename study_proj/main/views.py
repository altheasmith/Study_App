from django.shortcuts import render
from django.views.generic import View
from microbiology.models import Bacterium
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse


class MainView(View):
    def get(self, request):
        bacterium = Bacterium.objects.get(id=1)
        context = {'bacterium':bacterium}
        return render(request,'main/index.html', context)

class AddView(View):
    def get(self, request, card_type):
        # card_type_dict = {
        #     'bac':BacteriumForm.as_p(),
        #     'vir':VirusForm.as_p(),
        #     'fun':FungusForm.as_p(),
        #     'par':ParasiteForm.as_p(),
        #     'dis':DiseaseForm.as_p(),
        #     'dru':DrugForm.as_p()
        #     }
        return HttpResponse('hello')
