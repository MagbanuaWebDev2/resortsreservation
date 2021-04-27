from django.shortcuts import render
from .models import Info,User

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

def NextPage(request):
	trh = Info.objects.all().order_by('Fullname')
	trh = Info.objects.all().order_by('reserve')
	trh = Info.objects.all().order_by('contact')
	trh = Info.objects.all().order_by('resort')
	trh = Info.objects.all().order_by('entrance')
	trh = Info.objects.all().order_by('admit')
	return render(request, 'resorts_hub.html', {'trh':trh})

def new_record(request):
	trh = User.objects.create()
	Info.objects.create(text=request.POST['Fullname'], trh=trh)
	Info.objects.create(text=request.POST['reserve'], trh=trh)
	Info.objects.create(text=request.POST['contact'], trh=trh)
	Info.objects.create(text=request.POST['resort'], trh=trh)
	Info.objects.create(text=request.POST['entrance'], trh=trh)
	Info.objects.create(text=request.POST['admit'], trh=trh)
	return redirect(f'/next/{trh.id}/')

def add_record(request, trh_id):
	trh = User.objects.create()
	Info.objects.create(text=request.POST['Fullname'], trh=trh)
	Info.objects.create(text=request.POST['reserve'], trh=trh)
	Info.objects.create(text=request.POST['contact'], trh=trh)
	Info.objects.create(text=request.POST['resort'], trh=trh)
	Info.objects.create(text=request.POST['entrance'], trh=trh)
	Info.objects.create(text=request.POST['admit'], trh=trh)
	return redirect(f'/next/{trh.id}/')


def view_record(request, User_Id):
	uId = User.objects.get(id=User_Id)
	return render (request, 'resorts_hub.html',{'uId':uId})



