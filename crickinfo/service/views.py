from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from service.models import Player

# Create your views here.
class PlayerAPIView(APIView):
	def post(self, request,format=None):
		data = request.data
		
		plyr = Player(name=data["name"],
			age=data["age"],
			gender=data["gender"])
		plyr.save()
		return Response("player creatyed..")
		#Player(**data)
class CPU(APIView):
	def get(self,request,format=None):
		return Response("4")
	def post(self):
		pass
	def put(self):
		pass
	def delete(self):
		pass
