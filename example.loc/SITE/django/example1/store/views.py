from django.shortcuts import render, get_object_or_404, redirect
from helpers.multirequest import multirequest
from helpers.serviceLayer import serviceGroup

from .models import *
from .forms import *

############################Section########################################
def groups(request):	
    return serviceGroup.getGroups(request)

def group (request, iid):
	return serviceGroup.getGroup(request, iid)

@multirequest
def groupedit(request, iid):
	return serviceGroup.makeGroupedit(request, iid)
		
@groupedit.POST
def groupedit (request, iid):
	return serviceGroup.makeGroupeditPost(request, iid)	

def groupdelete( request, iid):
	return serviceGroup.makeGroupdelete(request, iid)
###########################Students############################

def students(request):
    allstudents = Student.objects.all()
    return render (request, 'store/students.html', locals())

def student (request, iid):
	student = Student.objects.get( pk = iid )
	return render (request, 'store/studentview.html', locals())


@multirequest
def studentedit(request, iid):
	s = get_object_or_404( Student, pk=iid)
	form = StudentForm (instance = s)
	return render (request, 'store/studentedit.html', locals())

@studentedit.POST
def studentedit (request, iid):
	s = get_object_or_404( Student, pk=iid)
	form = StudentForm (instance = s)
	form = StudentForm(request.POST)
	if form.is_valid() :
		s = get_object_or_404 (Student, pk=iid)
		s.fioStudent = form.cleaned_data['fioStudent']
		s.faculty = form.cleaned_data['faculty']
		s.healthGroup = form.cleaned_data['healthGroup']
		s.sectionStudent = form.cleaned_data['sectionStudent']
		s.save()
		return redirect ('store:students')
	else :
		return render (request, 'store/studentedit.html', locals())
		#return redirect ('store:groupedit',  iid)
		
#######################################################################


    
