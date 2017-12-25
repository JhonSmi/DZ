from django.shortcuts import render, get_object_or_404, redirect
from helpers.multirequest import multirequest

from .models import *
from .forms import *

############################Section########################################
def groups(request):
    allgroups = Section.objects.all()
    return render (request, 'store/groups.html', locals())

def group (request, iid):
	g = Section.objects.get( pk = iid )
	allst = Student.objects.filter( sectionStudent_id__exact = iid)
	return render (request, 'store/groupview.html', locals())


@multirequest
def groupedit(request, iid):
	g = get_object_or_404( Section, pk=iid)
	form = SectionForm (instance = g)
	return render (request, 'store/groupedit.html', locals())
		
@groupedit.POST
def groupedit (request, iid):
	g = get_object_or_404( Section, pk=iid)
	form = SectionForm (instance = g)
	form = SectionForm(request.POST)
	if form.is_valid() :
		g = get_object_or_404 (Section, pk=iid)
		g.title = form.cleaned_data['title']
		g.teacher = form.cleaned_data['teacher']
		#g.datetime = form.cleaned_data['datetime']
		g.level = form.cleaned_data['level']
		g.save()
		return redirect ('store:groups')
	else :
		return render (request, 'store/groupedit.html', locals())
		#return redirect ('store:groupedit',  iid)

def groupdelete( request, iid):
	g = get_object_or_404( Section, pk=iid)
	g.delete()
	return redirect ('store:groups')

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
		
