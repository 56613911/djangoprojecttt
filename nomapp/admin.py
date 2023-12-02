# nomapp/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Patient, Medic

class CustomUserAdmin(UserAdmin):
 
    list_display = UserAdmin.list_display + ('is_patient', 'is_medic')

    def is_patient(self, obj):
        return obj.is_patient()
    
    def is_medic(self, obj):
        return obj.is_medic()

    is_patient.boolean = True
    is_patient.short_description = 'Is Patient'

    is_medic.boolean = True
    is_medic.short_description = 'Is Medic'

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Patient)
admin.site.register(Medic)
