from django.db import models
from datetime import datetime

class Cathegory(models.Model):
    title       = models.CharField ( max_length=255, null=False, blank=False, unique=True )
    responser   = models.CharField ( max_length=255, null=True)
    created     = models.DateTimeField ('data created', default=datetime.now())
    level       = models.IntegerField(null=False,default=0)
    comment     = models.TextField(null=True)
