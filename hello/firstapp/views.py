from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.http import *
from django.shortcuts import render
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person


def index(request):
        userform = UserForm(field_order=["age", "name"])
        return render(request, "firstapp/index.html", {"form": userform})
        people = Person.objects.all()
        return render(request, "index.html", {"people": people})
def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")


def about(request):
    return HttpResponse("firstapp/about.html")


def contact(request):
    return HttpResponseRedirect("/")


def details(request):
    return HttpResponsePermanentRedirect("/")
