from django.contrib import admin
from microbiology.models import Bacterium, Virus, Fungus, Parasite

admin.site.register(Bacterium)
admin.site.register(Virus)
admin.site.register(Fungus)
admin.site.register(Parasite)
