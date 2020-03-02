from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .forms import NameForm2

def g_name(request):
    # context = {'form':"form"}
    form=NameForm2()
    return render(request, "demoapp2/index.html", {'form':form})

def index(request):
    return HttpResponse("This is from views file")