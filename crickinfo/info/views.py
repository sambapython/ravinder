from django.shortcuts import render
from django.http import HttpResponse
from service.models import Country


# Create your views here.
def createcountryview(request):
	msg=""
	if request.method=="POST":
		data = request.POST
		c=Country(name=data["name"])
		c.save()
		msg="country created successfully"
	return render(request,"info/create_country.html",
		{"message":msg})
