from django.contrib import admin
from .models import Bouee, DonneesGnss, DonneesCapteures
# Register your models here.
admin.site.register(Bouee)
admin.site.register(DonneesGnss)
admin.site.register(DonneesCapteures)