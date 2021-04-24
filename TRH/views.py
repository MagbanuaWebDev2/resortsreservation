#from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    '''return HttpResponse('homepage')
    if request.method == 'POST':
    	return HttpResponse(request.POST['Fullname'])
    return render(request,'homepage.html')'''  

def homepage(request):
	return render(request,'homepage.html', {'newPerson': request.POST.get('Fullname'),'newDate': request.POST.get('reserve'),'contactno': request.POST.get('contact'),'resortname': request.POST.get('resort'),'entrance': request.POST.get('admit'), 'aquant': request.POST.get('admitquant')})
