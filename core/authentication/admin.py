from django.contrib import admin

from core.authentication.models import User, Athlete, Personal

admin.site.register(User)
admin.site.register(Athlete)
admin.site.register(Personal)

# Register your models here.
