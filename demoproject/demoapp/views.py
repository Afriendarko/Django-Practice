from django.shortcuts import render, redirect
from . import forms
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Your data is entered succesfully")


def teapp(request):
    context = {'tag_vars': "tag_vars"}
    return render(request, "demoapp/index.html", context)


from .forms import NameForm

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


#
# def create(request):
#     if request.method=="POST":
#         form=forms.Loginform(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 return redirect('/success')
#             except:
#                 print("error here")
#     else:
#         form=forms.Loginform()
#     return render(request, 'myapp/home.html', {'form':form})