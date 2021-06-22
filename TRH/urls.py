from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name="home"),
	path('reserve', views.secondpage, name='reserve'),
	path('new', views.AnotherPage, name="new"),
	path('date', views.NextPage, name="date"),
	path('success', views.LastPage, name="success"),
	path('carddetails', views.Extra, name="carddetails"),
	path('delete/<int:id>', views.destroy),

]






# from django.conf.urls import url
# from . import views

# urlpatterns = [
# 	url(r'^$', views.MainPage, name='mainpage'),
# 	url(r'^RonanRev/(\d+)/$', views.ViewList, name='viewlist'),
# 	url(r'^RonanRev/newlist_url$', views.NewList, name='newlist'),
# 	url(r'^RonanRev/(\d+)/addItem$', views.AddItem, name='additem'),	
# ]