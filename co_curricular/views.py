from django.http import HttpResponse 

def index(request):
	return HttpResponse("<h1>Co- Curricular Page here </h1>")