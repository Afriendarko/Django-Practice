from django.shortcuts import render, redirect
from rest_framework import generics
from . import forms
from .forms import NameForm
from .models import Songs
from .serializers import SongsSerializer
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Your data is entered succesfully")


def teapp(request):
    context = {'tag_vars': "tag_vars"}
    return render(request, "demoapp/index.html", context)



def get_name(request):
    # context = {'form':"form"}
    form=NameForm()
    return render(request, "demoapp/index.html", {'form':form})

from .forms import mf

def modform(request):
    if request.method == 'POST':
        form = forms.mf(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/demoapp/success')

    else:
        form=forms.mf()
    return render(request, "demoapp/index.html", {'formset':form})

class ListSongsView(generics.ListAPIView):
    queryset = Songs.objects.all()
    serializer_class = SongsSerializer