from django.db import models

class Customer(models.Model):
	name = models.TextField(default="")
	contact = models.CharField(max_length=11, null=True)
	email = models.CharField(max_length=100, null=True)

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
	tot_amount = models.IntegerField(default='0')


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
	resortchosen = models.ForeignKey(Resort, null=True,  on_delete=models.CASCADE)
	
	








# from django.db import models

# class Customer(models.Model):
# 	name = models.TextField(default="")
# 	contact = models.CharField(max_length=11, null=True)
# 	reserve = models.DateField(null=True)

# 	def __str__(self):
# 		return self.name

# class Resort(models.Model):
# 	customerId=models.ManyToManyField(Customer)
# 	rchoice=(('Tubigan','Tubigan Garden Resort'),('Saniya', 'Saniya Resort & Hotel'),
# 	('Coco Valley', 'Coco Valley Richnez Waterpark'),('Volets','Volets Hotel & Resort'))
# 	resort = models.TextField(choices=rchoice, default='none')

# 	def __str__(self):
# 		return self.resort

# class Admission(models.Model):
# 	ResortId = models.ForeignKey(Resort, default=None, on_delete=models.CASCADE)
# 	entrchoice=(('Day','Day [Adult]'),('Night', 'Night [Adult]'),
# 		('Overnight', 'Overnight [Adult'))
# 	entrance = models.CharField(max_length=10, choices=entrchoice, default='none')
# 	admit = models.IntegerField(default='1')

# 	def __str__(self):
# 		return self.entrance

# class Cottage(models.Model):
# 	ResortID = models.ForeignKey(Resort, default=None, on_delete=models.CASCADE)
# 	cottagechoice=(('cottagea','Small Kubo [5 pax]'),('cottageb', 'Big Kubo [10 pax]'),
# 		('cottagec', 'Cavana [11-20 pax]'), ('cottaged', 'Full Cavana [30 pax]'))
# 	cottage = models.CharField(max_length=10, choices=cottagechoice, default='none')

# 	def __str__(self):
# 		return self.cottage






	

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
	
	


