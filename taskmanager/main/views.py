from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render


def glavnaya(request):
    return render(request, 'main/glavnaya.html')


def imported(request):
    return render(request, 'main/imported.html')


def analog(request):
    return render(request, 'main/analog.html')


def finalPrice(request):
    return render(request, 'main/finalPrice.html')


def authorisation(request):
    return render(request, 'main/authorisation.html')


def glavnayaAuthorised(request):
    return render(request, 'main/glavnayaAuthorised.html')


def history(request):
    return render(request, 'main/history.html')


