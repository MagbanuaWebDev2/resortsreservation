from django.shortcuts import render
from .models import Info

def homepage(request):

	if request.method == 'POST':
		Fullname = request.POST['Fullname']
		reserve = request.POST['reserve']
		contact = request.POST['contact']
		resort = request.POST['resort']
		entrance = request.POST['entrance']
		admit = request.POST['admit']

		trh1 = Info()
		trh1.Fullname = Fullname
		trh1.reserve = reserve
		trh1.contact = contact
		trh1.resort = resort
		trh1.entrance = entrance
		trh1.admit = admit
		trh1.save()

	return render(request,'homepage.html')

# def Viewrecords(request, UserId)
# 	uId = User.objects.get(id=UserId)
# 	return render (request, 'resorts_hub.html',{'uId':uId})

def NextPage(request):
	trh = Info.objects.all().order_by('Fullname')
	return render(request, 'resorts_hub.html',{'trh':trh})
