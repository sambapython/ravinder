from django.db import models

# Create your models here.
class Player(models.Model):
	gender_choices = [("male", "male"),("female","female")]
	name = models.CharField(max_length=250)
	age = models.IntegerField()
	gender = models.CharField(choices=gender_choices, max_length=7)
	class Meta:
		db_table="players"



