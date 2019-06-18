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
	def get(self, request, pk=None,format=None):
		if pk:
			players = Player.objects.filter(id=pk)
		else:
			players = Player.objects.all()
		data = [{"name":i.name,"age":i.age,"gender":i.gender } for i in players]
		return Response(data)

	def put(self, request, pk, format=None):
		players = Player.objects.filter(id=pk)
		if players:
			data = request.data
			players.update(**data)
			msg="player updated successfully"
		else:
			msg = "player not found"
		return Response(msg)

	def delete(self, request, pk, format=None):
		players = Player.objects.get(id=pk)
		players.delete()
		msg="player deleted successfully!!!"
		return Response(msg)
		
class CPU(APIView):
	def get(self,request,format=None):
		return Response("4")
	def post(self):
		pass
	def put(self):
		pass
	def delete(self):
		pass
