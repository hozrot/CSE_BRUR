from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
	return render(request,'base.html')

def log_in(request):
	return render(request,'log_in.html')
	
def sign_in(request):
	return render(request,'sign_in.html')
