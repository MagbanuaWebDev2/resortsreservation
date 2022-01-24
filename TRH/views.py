from django.shortcuts import redirect,render
from .forms import CardForm
from .models import Resort, Customer, Reservation, Card, Parking

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


	guest=Customer.objects.last

	return render(request,'nextpage.html', {
		'guest': guest}
	)

def NextPage(request):

	resortId=Resort.objects.create(
		resort = request.POST['resort'],
		entrance = request.POST['entrance'],
		admit = request.POST['admit'],
		pricea = request.POST['pricea'],
		cottage = request.POST['cottage'],
		quant = request.POST['quant'],
		priceb = request.POST['priceb'],
		tot_amount=request.POST['tot_amount'])

	park=Parking.objects.create(
		vehicle = request.POST['vehicle'],
		licenseplate = request.POST['licenseplate'],
		prkamnt = request.POST['prkamnt'])

	guest=Customer.objects.last
	enter=Resort.objects.last

	return render(request,'thirdpage.html', {
		'guest':guest,
		'enter':enter})

def LastPage(request):

	reserve=Reservation.objects.create(
		reserve=request.POST['reserve'])

	crdtcard=Card.objects.create(
		cardname = request.POST['cardname'],
		cardnum = request.POST['cardnum'],
		expmonth= request.POST['expmonth'],
		expyear= request.POST['expyear'],
		code = request.POST['code'])


	guest=Customer.objects.last
	enter=Resort.objects.last
	plan=Reservation.objects.last
	car=Parking.objects.last

	return render(request,'receipt.html', {
		'guest':guest,
		'enter':enter,
		'plan':plan,
		'car':car}
	)

def Extra(request):

	guest=Customer.objects.last
	enter=Resort.objects.last
	card=Card.objects.last

	return render(request,'card.html', {
		'guest':guest,
		'enter':enter,
		'card':card}
	)

def edit(request,id):
	card = Card.objects.get(id=id)
	return render(request,'edit.html',{'card':card})

def update(request,id):
    card = Card.objects.get(id=id)
    card.cardname = request.POST['cardname']
    card.cardnum = request.POST['cardnum']
    card.expmonth = request.POST['expmonth']
    card.expyear = request.POST['expyear']
    card.code = request.POST['code']
    card.save()
    return redirect("/carddetails")

def destroy(request,id):
	card = Card.objects.get(id=id)
	card.delete()
	return redirect("/carddetails")
