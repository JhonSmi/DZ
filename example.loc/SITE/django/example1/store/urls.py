from django.conf.urls import url
from . import views
 
urlpatterns = [
   # url( r'^$',views.index, name ='index'  ),
   url( r'^groups$',views.groups, name ='groups'  ),
   url( r'^group/(?P<iid>\d+)$', views.group, name='group' ),
   url( r'^groupedit/(?P<iid>\d+)$', views.groupedit, name='groupedit'),
]
