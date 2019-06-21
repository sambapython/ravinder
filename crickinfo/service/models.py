from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
	mobile = models.CharField(max_length=10,blank=True, null=True)
class abst(models.Model): # abstract model
	name = models.CharField(max_length=250)
	class Meta:
		abstract=True
class Player(abst):
	gender_choices = [("male", "male"),("female","female")]
	#name = models.CharField(max_length=250)
	age = models.IntegerField()
	gender = models.CharField(choices=gender_choices, max_length=7)
	class Meta:
		db_table="players"
	def __str__(self):
		return self.name
class Country(abst):
	#name = models.CharField(max_length=250, unique=True)
	def __str__(self):
		return self.name

class Match(models.Model):
	country1 = models.ForeignKey(Country, related_name="country1", on_delete=models.PROTECT)
	country2 = models.ForeignKey(Country, related_name="country2", on_delete=models.PROTECT)
	players = models.ManyToManyField(Player)






