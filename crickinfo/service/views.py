from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from service.models import Player, Match,Country
from service.serializers import MatchSerializer, MathcGetSerializer
from rest_framework import status
#from django.contrib.auth.models import User
from service.models import UserProfile
from rest_framework.authtoken.models import Token

class UserAPIView(APIView):
	authenctication_classes = []
	permission_classes=[]
	def post(self, request, format=None):
		data = request.data
		username = data['username']
		user = UserProfile.objects.filter(username=username)
		if user:
			user=user[0]
			tk = Token.objects.filter(user=user)
			if tk:
				token = tk[0].key
			else:
				tk = Token(user=user)
				tk.save()
				token = tk.key
		else:
			user = UserProfile.objects.create_user(username=username,password="12345678")
			tk = Token(user=user)
			tk.save()
			token = tk.key
		message = {"username":username, "token":token}
		return Response(message)
class MatchAPIView(APIView):

	def post(self, request,format=None):
		data = request.data
		ser = MatchSerializer(data=data)
		if ser.is_valid():
			countries = data["countries"]
			country1 = Country.objects.get(name=countries[0])
			country2 = Country.objects.get(name=countries[1])
			match = Match(country1=country1, country2=country2)
			match.save()
			for player in data["players"]:
				plr = Player.objects.get(name=player)
				match.players.add(plr)
			return Response("match created successfully!!")
		else:
			errors = ser._errors
			return Response(errors,status=status.HTTP_400_BAD_REQUEST)

	def get(self, request,pk=None, format=None):
		data = Match.objects.all()
		#resp = [{"countries":[match.country1.name, match.country2.name],
		#"players":[plr.name for plr in match.players.all()]} for match in data]
		ser = MathcGetSerializer(data, many=True)
		return Response(ser.data)


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
