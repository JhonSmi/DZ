from django.shortcuts import render

from .models import *

def groups(request):
    allgroups = Cathegory.objects.all()
    return render (request, 'store/groups.html', locals())

def group (request, iid):
	g = Cathegory.objects.get( pk = iid )
	return render (request, 'store/groupview.html', locals())