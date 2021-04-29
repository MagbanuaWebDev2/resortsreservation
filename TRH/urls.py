from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage),
	path('success', views.NextPage, name="success"),
	path('record', views.ThirdPage, name="record"),
]