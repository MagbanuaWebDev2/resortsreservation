from django.conf.urls import url
from TRH import views

urlpatterns = [
	url(r'^$', views.homepage, name='homepage.html'),
]
