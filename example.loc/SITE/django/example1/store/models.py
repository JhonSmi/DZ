from django.db import models
from datetime import datetime

class Section (models.Model):
    title       = models.CharField ( max_length=255, null=False, blank=False, unique=True )
    teacher     = models.CharField ( max_length=255, null=True)
    datetime     = models.DateTimeField ('data created', default=datetime.now())
    level       = models.IntegerField(null=False,default=0)
    
