from django.shortcuts import render
from django.http import HttpResponse 
from study.models import Teacher


# def index(request):
# 	teachers=Teacher.objects.exclude()
# 	return render(request,'study/index.html'),{
# 		'teachers' : teachers,

# 	}
def index(request):
		return render(request,'study/index.html')

def detail_teacher(request):
		return render(request,'study/detail.html')



