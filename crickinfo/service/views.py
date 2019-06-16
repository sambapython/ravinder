from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class CPU(APIView):
	def get(self,request,format=None):
		return Response("4")
	def post(self):
		pass
	def put(self):
		pass
	def delete(self):
		pass
