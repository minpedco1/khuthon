from django.shortcuts import render
from django.http import HttpResponse

#def index(request):
#    return HttpResponse("testing")

def index(request):
    return render(request, 'main.html')

def univBT(request):
    return render(request, 'univBT.html')

def comBT(request):
    return render(request, 'comBT.html')

def leftStudent(request):
    return render(request, 'leftStudent.html')

def leftUniv(request):
    return render(request, 'leftUniv.html')

def rightUniv(request):
    return render(request, 'rightUniv.html')

def rightEmp(request):
    return render(request, 'rightEmp.html')


