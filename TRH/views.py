from django.shortcuts import redirect,render
from .models import Admission, Resort, Customer, Cottage, Reservation, Card
# from .models import User, Info

def homepage(request):

	return render(request,'homepage.html')

def AnotherPage(request):

	customerId=Customer.objects.create(
		firstname = request.POST['firstname'],
		lastname = request.POST['lastname'],
		contact = request.POST['contact'],
		email = request.POST['email']
		)

	# ReservationId=Reservation.objects.create(
	# 	reserve = request.POST['reserve'])

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


	reserve=Reservation.objects.create(
		reserve=request.POST['reserve'],
		tot_amount=request.POST['tot_amount'])

	#	crdtcard=Card.objects.create(
		# cardname = request.POST['cardname'],
		# expdate = request.POST['expdate'],
		# code = request.POST['code'])

	d=Customer.objects.last
	c=Resort.objects.last
	b=Admission.objects.last
	a=Cottage.objects.last
	obj=Reservation.objects.last

	return render(request,'receipt.html', {
		'obj':obj,
		'a':a,
		'b':b,
		'c':c,
		'd':d}
	)











		# if request.method == 'POST':
		# customerId = Customer.objects.create(
		# 	name = request.POST['name'],
		# 	reserve = request.POST['reserve'],
		# 	contact = request.POST['contact'])

		# return redirect('weh')

		# mvg = Customer()
		# mvg.name = name
		# mvg.reserve = reserve
		# mvg.contact = contact
		# mvg.save()







#papasa kay sir dong tentative
# from django.shortcuts import redirect,render
# from .models import Admission, Resort, Customer, Cottage, Reservation, Card

# def homepage(request):

# 	return render(request,'homepage.html')

# def AnotherPage(request):

# 	customerId=Customer.objects.create(
# 		name = request.POST['name'],
# 		contact = request.POST['contact'],
# 		email = request.POST['email']
# 		)

# 	resortId=Resort.objects.create(
# 		resort = request.POST['resort'])

# 	return render(request,'nextpage.html')

# def NextPage(request):

# 	admit=Admission.objects.create(
# 		entrance = request.POST['entrance'],
# 		admit = request.POST['admit'],
# 		pricea = request.POST['pricea']
# 		)

# 	cottage=Cottage.objects.create(
# 		cottage = request.POST['cottage'],
# 		quant = request.POST['quant'],
# 		priceb = request.POST['priceb'])

# 	reserve=Reservation.objects.create(
# 		reserve=request.POST['reserve'],
# 		tot_amount=request.POST['tot_amount'])

#	crdtcard=Card.objects.create(
		# cardname = request.POST['cardname'],
		# expdate = request.POST['expdate'],
		# code = request.POST['code'])

# 	return render(request,'receipt.html')

