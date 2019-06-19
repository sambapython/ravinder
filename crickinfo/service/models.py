from django.db import models

# Create your models here.
class Player(models.Model):
	gender_choices = [("male", "male"),("female","female")]
	name = models.CharField(max_length=250)
	age = models.IntegerField()
	gender = models.CharField(choices=gender_choices, max_length=7)
	class Meta:
		db_table="players"
class Country(models.Model):
	name = models.CharField(max_length=250, unique=True)

class Match(models.Model):
	country1 = models.ForeignKey(Country, related_name="country1", on_delete=models.PROTECT)
	country2 = models.ForeignKey(Country, related_name="country2", on_delete=models.PROTECT)
	players = models.ManyToManyField(Player)




