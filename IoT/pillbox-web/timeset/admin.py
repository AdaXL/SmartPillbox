# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Patient, Medicine, Pi

#class PatientAdmin(admin.ModelAdmin):
#	list_display = ('patient_name')
	
class MedicineAdmin(admin.ModelAdmin):
	list_display = ('patient', 'medicine_text', 'time')
	list_filter = ('patient', 'medicine_text')
	# search_fields = ('patient', 'medicine_text')
	# prepopulated_fields = {'slug':('medicine_text',)}
	# raw_id_fields = ('patient',)
	
class PiAdmin(admin.ModelAdmin):
	list_display = ('patient', 'Pi_ip')
	
admin.site.register(Patient)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Pi)
