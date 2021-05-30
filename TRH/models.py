from django.db import models

class Card(models.Model):	
	cardname = models.TextField()
	expdate = models.DateField()
	code = models.CharField(max_length=4)

class Customer(models.Model):
	name = models.CharField(max_length=20)
	contact = models.CharField(max_length=11)
	email = models.EmailField(max_length=100)
	card = models.OneToOneField(Card, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

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
	
	def __str__(self):
		return self.resort

class Admission(models.Model):
	resorts = models.OneToOneField(Resort, null=True, on_delete=models.CASCADE)
	entrance = models.CharField(max_length=30)
	admit = models.IntegerField(default='1')
	pricea = models.IntegerField(default='100')

	def get_entrance_display(self):
		return

	def __str__(self):
		return self.entrance

class Cottage(models.Model):
	resorts = models.OneToOneField(Resort, null=True, on_delete=models.CASCADE)
	cottage = models.CharField(max_length=100)
	quant = models.IntegerField()
	priceb = models.IntegerField()

	def __str__(self):
		return self.cottage

class Reservation(models.Model):
	reserve = models.DateField(null=True)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	resortchosen = models.ForeignKey(Resort, null=True, on_delete=models.CASCADE)
	tot_amount = models.IntegerField(default='0')

	












	# cotchoice=(
	# 	('1','Small Kubo (6 pax)'),
	# 	('2', 'Medium Kubo (12 pax)'),
	# 	('3', 'Large Kubo (15 pax)'),
	# 	('4', 'Open Kubo (20 pax)'),
	# 	('5', 'Gazebo (9 pax)'),
	# 	('6', 'Gazebo (4 pax)'),
	# 	('7', 'Small Kubo (8 pax)'),
	# 	('8', 'Medium Kubo (10 pax)'),
	# 	('9', 'Large Kubo (15 pax)'),
	# 	('10', 'Peach Cottage (10 pax)'),
	# 	('11', 'Violet Cottage (25 pax)'),
	# 	('12', 'Small Kubo (5 pax)'),
	# 	('13', 'Big Kubo (8-10 pax)'),
	# 	('14', 'Small Cavana (8 pax)'),
	# 	('15', 'Kubo Cavana (10-12 pax)'),
	# 	('16', 'Full Cavana (20 pax)'),
	# 	('17', 'Umbrella (4 pax)'),
	# 	('18', 'Short Table (6 pax)'),
	# 	('19', 'Petits Cottage (10 pax)'),
	# 	('20', 'Grande Cottage (20 pax)'),
	# 	('21', 'Big Nipa Hut (30 pax)'),
	# 	('22', 'Regular Cottage (10 pax)'),
	# 	('23', 'Big Cottage (25 pax)'),
	# 	('24', 'Bahay Kubo (2 pax)'),
	# 	('25', 'Regular Cottage (10 pax)'),
	# 	('26', 'Regular Cottage (16 pax)'),
	# 	('27', 'Small Kubo (8 pax)'),
	# 	('28', 'Big Kubo (10 pax)'),
	# 	('29', 'Tent (6 pax)'),
	# 	('30', 'Table with Umbrella (4 pax)'),
	# 	('31', 'Regular Cottage (15-20 pax)'),
	# 	('32', 'Table (8-10 pax)'),
	# 	('33', 'Umbrella (4 pax)'),
	# 	('34', 'Family Kubo (20 pax)'),
	# 	('35', 'Kubo with sink (12 pax)'),
	# 	('36', 'Table (6 pax)'),
	# 	('37', 'Regular Cottage (8 pax)'),
	# 	('38', 'Regular Cottage (12 pax)'),
	# 	('39', 'Regular Cottage (15 pax)'),
	# 	('40', 'Gazebo Kubo (15 pax)'),
	# 	('1500', 'Elevated Floor (20 pax)')

	# )

	# 	entrchoice=(
	# 	('200','Day'),
	# 	('200', 'Night'),
	# 	('150', 'Day'),
	# 	('180', 'Night'),
	# 	('180', 'Overnight'),
	# 	('150', 'Day'),
	# 	('180', 'Night'),
	# 	('180', 'Overnight'),
	# 	('250', 'Day'),
	# 	('250', 'Night'),
	# 	('300', 'Overnight'),
	# 	('200', 'Day'),
	# 	('250', 'Night'),
	# 	('300', 'Overnight'),
	# 	('150', 'Day'),
	# 	('170', 'Night'),
	# 	('130', 'Day'),
	# 	('100', 'Day'),
	# 	('120', 'Night'),
	# 	('150', 'Overnight'),
	# 	('130', 'Day'),
	# 	('150', 'Night'),
	# 	('170', 'Overnight'),
	# 	('200', 'Day')

	# )
