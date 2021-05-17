from django.db import models

class Card(models.Model):	
	cardname = models.TextField()
	expdate = models.DateField()
	code = models.CharField(max_length=4)

class Customer(models.Model):
	name = models.TextField()
	contact = models.CharField(max_length=11)
	email = models.CharField(max_length=100)
	card = models.OneToOneField(Card, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class Admission(models.Model):
	# ResortId = models.ForeignKey(Resort, default=None, on_delete=models.CASCADE)
	# resort = models.OneToOneField(Resort, on_delete=models.CASCADE)
	entrchoice=(
		('150','Day'),
		('200', 'Night'),
		('250', 'Overnight')
	)
	entrance = models.CharField(max_length=50, choices=entrchoice)
	admit = models.IntegerField(default='1')
	pricea = models.IntegerField(default='150')

class Cottage(models.Model):
	# ResortID = models.ForeignKey(Resort, default=None, on_delete=models.CASCADE)
		# resort = models.OneToOneField(Resort, on_delete=models.CASCADE)
	cottagechoice=(
		('Small Kubo [5 pax]','Small Kubo [5 pax]'),
		('Big Kubo [10 pax]', 'Big Kubo [10 pax]'),
		('Cavana [11-20 pax]', 'Cavana [11-20 pax]'), 
		('Full Cavana [30 pax]', 'Full Cavana [30 pax]')
	)
	cottage = models.TextField(choices=cottagechoice)
	quant = models.IntegerField(default='100')
	priceb = models.IntegerField(default='300')

	def __str__(self):
		return self.cottage

class Resort(models.Model):
	# customerId=models.ManyToManyField(Customer)
	rchoice=(
		('Tubigan Garden Resort','Tubigan'),
		('Saniya Resort & Hotel', 'Saniya'),
		('Coco Valley Richnez Waterpark', 'Coco Valley'),
		('Volets Hotel & Resort','Volets')
	)
	resort = models.TextField(choices=rchoice, default='none')
	admission = models.OneToOneField(Admission, null=True, on_delete=models.CASCADE)
	cottage = models.OneToOneField(Cottage, null=True, on_delete=models.CASCADE)

	def __str__(self):
		return self.resort

class Reservation(models.Model):
	reserve = models.DateField(null=True)
	customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
	resortchosen = models.ForeignKey(Resort, null=True, on_delete=models.CASCADE)
	tot_amount = models.IntegerField(default='0')
	



	

#eto papasa kay sir tentative

# from django.db import models

# class Customer(models.Model):
# 	name = models.TextField(default="")
# 	contact = models.CharField(max_length=11, null=True)
# 	email = models.CharField(max_length=100, null=True)

# 	def __str__(self):
# 		return self.name

# class Admission(models.Model):
# 	# ResortId = models.ForeignKey(Resort, default=None, on_delete=models.CASCADE)
# 	# resort = models.OneToOneField(Resort, on_delete=models.CASCADE)
# 	entrchoice=(
# 		('Day','Day'),
# 		('Night', 'Night'),
# 		('Overnight', 'Overnight')
# 	)
# 	entrance = models.TextField(choices=entrchoice)
# 	admit = models.IntegerField(default='1')
	
# 	def __str__(self):
# 		return self.entrance

# class Cottage(models.Model):
# 	# ResortID = models.ForeignKey(Resort, default=None, on_delete=models.CASCADE)
# 		# resort = models.OneToOneField(Resort, on_delete=models.CASCADE)
# 	cottagechoice=(
# 		('Small Kubo [5 pax]','Small Kubo [5 pax]'),
# 		('Big Kubo [10 pax]', 'Big Kubo [10 pax]'),
# 		('Cavana [11-20 pax]', 'Cavana [11-20 pax]'), 
# 		('Full Cavana [30 pax]', 'Full Cavana [30 pax]')
# 	)
# 	cottage = models.TextField(choices=cottagechoice)
#	quant = models.IntegerField(default='1')

# 	def __str__(self):
# 		return self.cottage

# class Resort(models.Model):
# 	# customerId=models.ManyToManyField(Customer)
# 	rchoice=(
# 		('Tubigan Garden Resort','Tubigan'),
# 		('Saniya Resort & Hotel', 'Saniya'),
# 		('Coco Valley Richnez Waterpark', 'Coco Valley'),
# 		('Volets Hotel & Resort','Volets')
# 	)
# 	resort = models.TextField(choices=rchoice, default='none')
# 	admission = models.OneToOneField(Admission, null=True, on_delete=models.CASCADE)
# 	cottage = models.OneToOneField(Cottage, null=True, on_delete=models.CASCADE)

# 	def __str__(self):
# 		return self.resort

# class Reservation(models.Model):
# 	reserve = models.DateField(null=True)
# 	customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
# 	resortchosen = models.ForeignKey(Resort, null=True,  on_delete=models.CASCADE)
	
	


