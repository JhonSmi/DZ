from django.shortcuts import render, get_object_or_404, redirect
from helpers.multirequest import multirequest

from .models import *
from .forms import *

def groups(request):
    allgroups = Section.objects.all()
    return render (request, 'store/groups.html', locals())

def group (request, iid):
	g = Section.objects.get( pk = iid )
	return render (request, 'store/groupview.html', locals())


@multirequest
def groupedit(request, iid):
	g = get_object_or_404( Section, pk=iid)
	return render (request, 'store/groupedit.html', locals())
		
@groupedit.POST
def groupedit (request, iid):
	form = SectionForm(request.POST)
	if form.is_valid() :
		g = get_object_or_404 (Section, pk=iid)
		g.title = form.cleaned_data['title']
		g.save()
		return redirect ('store:groups')
	else :
		return redirect ('store:groupedit',  iid)