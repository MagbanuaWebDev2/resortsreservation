from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
	path('new', views.AnotherPage, name="new"),
	path('success', views.NextPage, name="success"),
	# path('success', views.Nextpage, name="success"),
]






# from django.conf.urls import url
# from . import views

# urlpatterns = [
# 	url(r'^$', views.MainPage, name='mainpage'),
# 	url(r'^RonanRev/(\d+)/$', views.ViewList, name='viewlist'),
# 	url(r'^RonanRev/newlist_url$', views.NewList, name='newlist'),
# 	url(r'^RonanRev/(\d+)/addItem$', views.AddItem, name='additem'),	
# ]