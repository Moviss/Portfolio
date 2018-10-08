from django.shortcuts import render

from .models import Tech

def home(request):
    techs = Tech.objects
    return render(request, 'techs/home.html', {'techs': techs})
