from django.db import models

class Card(models.Model):	
	cardname = models.CharField(max_length=50, null=True)
	cardnum = models.CharField(max_length=20, null=True)
	expmonth = models.CharField(max_length=8, null=True)
	expyear = models.CharField(max_length=4, null=True)
	code = models.CharField(max_length=3, null=True)


class Customer(models.Model):
	firstname = models.CharField(max_length=20)
	lastname = models.CharField(max_length=20)
	contact = models.CharField(max_length=11)
	email = models.EmailField(max_length=100)
	card = models.OneToOneField(Card, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.firstname

class Parking(models.Model):
	customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	vehicletype = (
		('0', 'None'),
		('10', 'Motorcycle'),
		('20', 'Tricycle'),
		('100', 'Jeepney'),
		('200', 'Van'),
		('250', 'Pickup Truck'),
		('150', 'Sedan')
	)
	vehicle = models.CharField(max_length=100, choices=vehicletype, null=True)
	licenseplate = models.CharField(max_length=13, null=True)
	prkamnt = models.IntegerField(null=True)

	def __str__(self):
		return self.vehicle

class Resort(models.Model):
	rchoice=(
		('Tubigan Garden Resort','Tubigan'),
		('Saniya Resort & Hotel', 'Saniya'),
		('Coco Valley Richnez Waterpark', 'Coco Valley'),
		('Volets Hotel & Resort','Volets'),
		('Jardin De Dasmarinas', 'Jardin'),
		('V Resort Dasmarinas', 'V'),
		('Palmas Del Sol Resort', 'Palmas Del Sol'),
		('Riverside Resort', 'Riverside'),
		('Qubo Qabana Resort', 'Qubo'),
		('Kalipayan Resort', 'Kalipayan')
	)
	resort = models.CharField(max_length=100, choices=rchoice, default='none')
	
	entrchoice=(
		('200','Day'),
		('250', 'Night'),
		('150', 'Day'),
		('180', 'Night'),
		('210', 'Overnight'),
		('170', 'Day'),
		('190', 'Night'),
		('220', 'Overnight'),
		('270', 'Day'),
		('280', 'Night'),
		('300', 'Overnight'),
		('230', 'Day'),
		('260', 'Night'),
		('310', 'Overnight'),
		('140', 'Day'),
		('185', 'Night'),
		('130', 'Day'),
		('100', 'Day'),
		('120', 'Night'),
		('160', 'Overnight'),
		('135', 'Day'),
		('155', 'Night'),
		('175', 'Overnight')

	)

	entrance = models.CharField(max_length=30, choices=entrchoice)
	admit = models.IntegerField(default='1')
	pricea = models.IntegerField(default='100')

	cotchoice=(
		('750','Small Kubo (6 pax)'),
		('1000', 'Medium Kubo (12 pax)'),
		('1200', 'Large Kubo (15 pax)'),
		('1250', 'Open Kubo (20 pax)'),
		('900', 'Gazebo (9 pax)'),
		('300', 'Gazebo (4 pax)'),
		('500', 'Small Kubo (8 pax)'),
		('600', 'Medium Kubo (10 pax)'),
		('800', 'Large Kubo (15 pax)'),
		('650', 'Peach Cottage (10 pax)'),
		('1300', 'Violet Cottage (25 pax)'),
		('400', 'Small Kubo (5 pax)'),
		('670', 'Big Kubo (8-10 pax)'),
		('700', 'Small Cavana (8 pax)'),
		('1400', 'Kubo Cavana (10-12 pax)'),
		('1800', 'Full Cavana (20 pax)'),
		('350', 'Umbrella (4 pax)'),
		('380', 'Short Table (6 pax)'),
		('550', 'Petits Cottage (10 pax)'),
		('850', 'Grande Cottage (20 pax)'),
		('2000', 'Big Nipa Hut (30 pax)'),
		('520', 'Regular Cottage (10 pax)'),
		('1220', 'Big Cottage (25 pax)'),
		('470', 'Bahay Kubo (2 pax)'),
		('450', 'Regular Cottage (10 pax)'),
		('630', 'Regular Cottage (16 pax)'),
		('420', 'Small Kubo (8 pax)'),
		('510', 'Big Kubo (10 pax)'),
		('340', 'Tent (6 pax)'),
		('330', 'Table with Umbrella (4 pax)'),
		('460', 'Regular Cottage (15-20 pax)'),
		('280', 'Table (8-10 pax)'),
		('250', 'Umbrella (4 pax)'),
		('1210', 'Family Kubo (20 pax)'),
		('620', 'Kubo with sink (12 pax)'),
		('310', 'Table (6 pax)')
	)

	cottage = models.CharField(max_length=100, choices=cotchoice)
	quant = models.IntegerField()
	priceb = models.IntegerField()
	tot_amount = models.IntegerField(default='0')


	
	def __str__(self):
		return self.resort


class Reservation(models.Model):
	reserve = models.DateField()
	customer = models.ManyToManyField(Customer)
	resortchosen = models.ManyToManyField(Resort)


	














