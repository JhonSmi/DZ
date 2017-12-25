from django.shortcuts import render, get_object_or_404, redirect
import store.models as sm
import store.forms  as fm
from helpers.rowDataGateway import GroupGateway

class serviceGroup (object):
 	
 	def getGroups(request):
 		allgroups = sm.Section.objects.all()
 		return render (request, 'store/groups.html', locals())

 	def getGroup(request, iid):
 		gr =  GroupGateway(iid = iid)
 		g = gr.getRowGroup()                                                                 #sm.Section.objects.get( pk = iid )
 		allst = sm.Student.objects.filter( sectionStudent_id__exact = iid)
 		return render (request, 'store/groupview.html', locals())

 	def makeGroupedit(request, iid):
 		g = get_object_or_404( sm.Section, pk=iid)
 		form = fm.SectionForm (instance = g)
 		return render (request, 'store/groupedit.html', locals())

 	def makeGroupeditPost(request, iid):
 		gr =  GroupGateway(iid = iid)
 		g = gr.getRowGroup() 
 		form = fm.SectionForm (instance = g)
 		form = fm.SectionForm(request.POST)
 		if form.is_valid() :
 			g =  GroupGateway(iid = iid, title = form.cleaned_data['title'], teacher = form.cleaned_data['teacher'],datetime = form.cleaned_data['datetime'], level = form.cleaned_data['level'])
 			g.setTitle()
 			g.setTeacher()
 			g.setDatetime()
 			g.setLevel()
 			return redirect ('store:groups')
 		else :
 			return render (request, 'store/groupedit.html', locals())

 	def makeGroupdelete(request, iid):
 		g =  GroupGateway(iid = iid)
 		g.deleteRowGroup()
 		return redirect ('store:groups')


