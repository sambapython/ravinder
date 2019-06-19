from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from service.models import Player, Match,Country

class MatchAPIView(APIView):
	def post(self, request,format=None):
		data = request.data
		countries = data["countries"]
		country1 = Country.objects.get(name=countries[0])
		country2 = Country.objects.get(name=countries[1])
		match = Match(country1=country1, country2=country2)
		match.save()
		for player in data["players"]:
			plr = Player.objects.get(name=player)
			match.players.add(plr)
		return Response("match created successfully!!")

	def get(self, request,pk=None, format=None):
		data = Match.objects.all()
		resp = [{"countries":[match.country1.name, match.country2.name],
		"players":[plr.name for plr in match.players.all()]} for match in data]
		return Response(resp)


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
