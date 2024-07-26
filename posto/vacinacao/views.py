from django.shortcuts import render
from django.http import HttpResponse
from .models import Criancas

# Create your views here.
def q1(request):
    resp = Criancas.objects.filter(nomeMae="Maria Antonieta").filter(vacina="")
    return HttpResponse(resp)

def q2(request):
    resp = Criancas.objects.filter(idade__gte=2, idade__lte=8)
    return HttpResponse(resp)

def q3(request):
    resp = Criancas.objects.filter(vacina__contains="Poliomielite", idade__gte=0 , idade__lte=3)
    return HttpResponse(resp)

def vacinada(request):
    resp = Criancas.objects.filter(bairro="Limeira")
    return HttpResponse(resp)

def q9(request):
    resp = Criancas.objects.filter(vacina=True).count()
    return HttpResponse(resp)