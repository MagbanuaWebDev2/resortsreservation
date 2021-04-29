from django.db import models

class User(models.Model):
	pass

class Info(models.Model):
	visitor = models.ForeignKey(User, default=None, on_delete=models.CASCADE, null=True)
	#Name
	Fullname = models.CharField(max_length=20, null=True)
	#Reservation Date
	reserve = models.DateField(null=True)
	#Contact No.
	contact = models.CharField(max_length=11, null=True)
	#ResortName
	rchoice=(('resorta','Tubigan Garden Resort'),('resortb', 'Saniya Resort & Hotel'),
		('resortc', 'Coco Valley Richnez Waterpark'),('resortd','Volets Hotel & Resort'))
	resort = models.CharField(max_length=10, choices=rchoice, default='none')
	entrchoice=(('entrancea','Day [Adult]'),('entranceb', 'Night [Adult]'),
		('entracec', 'Overnight [Adult'))
	entrance = models.CharField(max_length=10, choices=entrchoice)
	#Quantity of Entrance
	admit = models.IntegerField(default='1')

def __str__(self):
	return self.name

