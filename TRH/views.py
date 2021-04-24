from django.shortcuts import render

def homepage(request):
	return render(request,'homepage.html', {'newPerson': request.POST.get('Fullname'),'newDate': request.POST.get('reserve'),'contactno': request.POST.get('contact'),'resortname': request.POST.get('resort'),'admit': request.POST.get('entrance'), 'aquant': request.POST.get('admitquant')})
