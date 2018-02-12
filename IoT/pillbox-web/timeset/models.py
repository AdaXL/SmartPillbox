# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Patient(models.Model):
	patient_name = models.CharField(max_length=200)
	def __str__(self):
		return self.patient_name

class Medicine(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	medicine_text = models.CharField(max_length=200)
	time = models.TimeField()
	def __str__(self):
		return self.medicine_text
		
class Pi(models.Model):
	patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
	Pi_ip = models.GenericIPAddressField()
	def __str__(self):
		return self.Pi_ip
