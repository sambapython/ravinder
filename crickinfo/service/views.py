from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from service.models import Player, Match,Country
from service.serializers import MatchSerializer, MathcGetSerializer,\
CpuSerializer, UserGetSerializer
from rest_framework import status
#from django.contrib.auth.models import User
from service.models import UserProfile
from rest_framework.authtoken.models import Token
from rest_framework.generics import GenericAPIView 
from django.conf import settings
import requests
from django.http import HttpResponse

def oauth2redirect_view(request,*args, **kwargs):
	code = request.GET.get("code")
	return HttpResponse(code)

def get_code_google_view(request):
	token_request_uri = "https://accounts.google.com/o/oauth2/auth"
	response_type = "code"
	client_id = settings.CLIENT_ID
	redirect_uri = "http://localhost:8000/oauth2redirect/"
	scope = "https://www.googleapis.com/auth/userinfo.profile https://www.googleapis.com/auth/userinfo.email"
	url = f"{token_request_uri}?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
	resp = requests.get(url)
	return HttpResponse(resp.text)
def get_google_auth_view(request):
	return render(request, "service/get_google_auth.html")

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
	def get(self, request, email=None,format=None):
		#params = request.query_params
		#email=params.get("email")
		if email:
			users = UserProfile.objects.filter(email=email)
		else:
			users = UserProfile.objects.all()
		if users:
			users = UserGetSerializer(users, many=True)
			return Response(users.data)
		else:
			return Response("No users found")

class MatchAPIView(GenericAPIView):
	serializer_class = MatchSerializer
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

		
class CPU(GenericAPIView ):
	serializer_class = CpuSerializer
	def post(self, request, format=None):
		pass