from django.shortcuts import render, get_object_or_404, redirect
import store.models as sm
import store.forms  as fm
import os.path

class GroupGateway(object):
	
	def __init__(self, **kwargs):
		if "iid" in kwargs:
			self.iid = int(kwargs["iid"])
		if "title" in kwargs:
			self.title = kwargs["title"]
		if "teacher" in kwargs:
			self.teacher = kwargs["teacher"]
		if "datetime" in kwargs:
			self.datetime = kwargs["datetime"]
		if "level" in kwargs:
			self.level = kwargs["level"]
		self.RowGroup = []


	def getRowGroup(self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		return self.RowGroup

	def deleteRowGroup (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.delete()
    
	def setTitle (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.title = self.title
		self.RowGroup.save()

	def setTeacher (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.teacher = self.teacher
		self.RowGroup.save()

	def setDatetime (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.datetime = self.datetime
		self.RowGroup.save()

	def setLevel (self):
		self.RowGroup = sm.Section.objects.get( pk = self.iid )
		self.RowGroup.level = self.level
		self.RowGroup.save()


    

    
    #def updateRowGroup (self):
    #	pass