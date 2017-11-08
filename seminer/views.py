from django.http import HttpResponse 

def index(request):
	return HttpResponse("<h1>Seminar Page here </h1>")