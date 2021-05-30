from django.shortcuts import redirect,render
from .models import Admission, Resort, Customer, Cottage, Reservation, Card
# from .models import User, Info

def homepage(request):

	return render(request,'homepage.html')

def AnotherPage(request):

	customerId=Customer.objects.create(
		name = request.POST['name'],
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





















# from django.shortcuts import redirect,render
# from .models import Admission, Resort, Customer, Cottage, Reservation
# # from .models import User, Info

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

# 	# ReservationId=Reservation.objects.create(
# 	# 	reserve = request.POST['reserve'])

# 	return render(request,'nextpage.html')

# def NextPage(request):

# 	# customer=Customer.objects.get(id=customer)
# 	# resort=Resort.objects.get(id=resort)


# 	admit=Admission.objects.create(
# 		entrance = request.POST['entrance'],
# 		admit = request.POST['admit'],
# 		tot_amount = request.POST['tot_amount']
# 		)

# 	cottage=Cottage.objects.create(
# 		cottage = request.POST['cottage'])

# 	reserve=Reservation.objects.create(
# 		reserve=request.POST['reserve'])

# 	return render(request,'receipt.html')

# # def Nextpage(request, customerId):

# # 	
	














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

