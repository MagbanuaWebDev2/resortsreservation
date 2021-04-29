from django.shortcuts import redirect,render
from . models import Info,User

def homepage(request):

	if request.method == 'POST':

		visitor = User.objects.create()
		Info.objects.create(
			Fullname = request.POST['Fullname'],
			reserve = request.POST['reserve'], 
			contact = request.POST['contact'],
			resort = request.POST['resort'], 
			entrance = request.POST['entrance'],
			admit = request.POST['admit'],
			)
		
		return redirect('success')

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
	trh = Info.objects.last()
	return render(request, 'receipt.html', {'trh':trh})


def view_receipt(request, visitor):
	uId = User.objects.get(id=visitor)
	return render (request, 'receipt.html',{'uId':uId})






























# def ThirdPage(request):
# 	trh = Info.objects.all().order_by('Fullname')
# 	trh = Info.objects.all().order_by('reserve')
# 	trh = Info.objects.all().order_by('contact')
# 	trh = Info.objects.all().order_by('resort')
# 	trh = Info.objects.all().order_by('entrance')
# 	trh = Info.objects.all().order_by('admit')
# 	return render(request, 'resorts_hub.html', {'trh':trh})











