from django.shortcuts import redirect,render
from .models import Admission, Resort, Customer, Cottage, Reservation, Card

def homepage(request):

	return render(request,'TRH.html')


def secondpage(request):

	return render(request,'homepage.html')


def AnotherPage(request):

	customerId=Customer.objects.create(
		firstname = request.POST['firstname'],
		lastname = request.POST['lastname'],
		contact = request.POST['contact'],
		email = request.POST['email']
		)

	
	# crdtcard=Card.objects.create(
	# 	cardname = request.POST['cardname'],
	# 	cardnum = request.POST['expdate'],
	# 	code = request.POST['code'])


	d=Customer.objects.last

	return render(request,'nextpage.html', {
		'd':d}
	)

def NextPage(request):

	resortId=Resort.objects.create(
		resort = request.POST['resort'])

	admit=Admission.objects.create(
		entrance = request.POST['entrance'],
		admit = request.POST['admit'],
		pricea = request.POST['pricea']
		)

	cottage=Cottage.objects.create(
		cottage = request.POST['cottage'],
		quant = request.POST['quant'],
		priceb = request.POST['priceb'])


	return render(request,'thirdpage.html')

def LastPage(request):

	reserve=Reservation.objects.create(
		reserve=request.POST['reserve'],)
		# tot_amount=request.POST['tot_amount']


	d=Customer.objects.last
	c=Resort.objects.last
	b=Admission.objects.last
	a=Cottage.objects.last

	return render(request,'receipt.html', {
		'a':a,
		'b':b,
		'c':c,
		'd':d}
	)


def Extra(request):
	return render(request,'card.html')
