'''from django.http import HttpResponse'''
from django.shortcuts import render

def homepage(request):
    '''return HttpResponse('homepage')'''
    if request.method == 'POST':
    	return HttpResponse(request.POST['Fullname'])
    return render(request,'homepage.html')
