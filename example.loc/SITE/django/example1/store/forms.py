# -*- coding: utf-8 -*-
from django import forms

from .models import *

class SectionForm(forms.ModelForm):
 	class Meta :
 		model = Section
 		fields = '__all__'