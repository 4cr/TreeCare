from django.db import models
#admin - adm1n1strat0r

# Create your models here.
class Account(models.Model):
	account_num = models.CharField(max_length=32)

	def __str__(self):
		return self.account_num

class Suburb(models.Model):
	name = models.CharField(max_length=32)
	comment = models.CharField(max_length=512, null=True)

	def __str__(self):
		return self.name

class WateringSession(models.Model):
	count = models.IntegerField(default=0)			# QTY
	genus = models.CharField(max_length=250)		# Genus / species
	volume = models.IntegerField(default=0)			# Litres / tree
	location = models.CharField(max_length=250)		# Location
	location_type = models.CharField(max_length=64)	# Location Type
	frequency = models.CharField(max_length=32)		# Frequency
	account = models.ForeignKey(Account)			# Account Number
	suburb = models.ForeignKey('Suburb')
	is_done = models.BooleanField(default=False)	# Done

	def __str__(self):
		return self.suburb.name + ' : ' + self.genus + ' / ' + self.location