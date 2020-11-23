from django.shortcuts import render, HttpResponse, redirect

from core.models import Evento


def hello(request, nome, idade):
    return HttpResponse('Hello Word {}! Voce tem {} anos!'.format(nome, idade))

def local(request, evento):
    return HttpResponse('Hello Word {}! Voce tem {} anos!')

def lista_eventos(request):
    evento = Evento.objects.all()
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)

def index(request):
    return redirect('/agenda/')