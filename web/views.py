from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import User, Games

# Create your views here.


def home(request):
    data = User.objects.all()
    template = loader.get_template('index.html')
    context = {
        'contoh':"hallo cukii",
        'home': data
    }
    return HttpResponse(template.render(context, request))


def menu(request):
    data = Games.objects.all()
    context = {
        'data' : data
    }

    return render(request, 'menu.html', context)
