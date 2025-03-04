from django.contrib import admin

from core.trainy.models import exercicies_divison, muscles, division, exercicies

admin.site.register(exercicies_divison.Exercicies_Division)
admin.site.register(muscles.Muscles)
admin.site.register(division.Division)
admin.site.register(exercicies.Exercicies)
