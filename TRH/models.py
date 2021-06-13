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

class Resort(models.Model):
	resort = models.CharField(max_length=100)
	
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
	reserve = models.DateField()
	customer = models.ManyToManyField(Customer)
	resortchosen = models.ManyToManyField(Resort)
	tot_amount = models.IntegerField(default='0')
	request = models.TextField(default='')



	














