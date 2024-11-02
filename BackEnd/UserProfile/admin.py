from django.contrib import admin

from .models import Profile, PersonalData, EducationalData, ProfessionalData

admin.site.register(Profile)
admin.site.register(PersonalData)
admin.site.register(EducationalData)
admin.site.register(ProfessionalData)