from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from core.models import Evento


@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos': evento}
    return render(request, 'agenda.html', dados)


@login_required(login_url='/login/')
def evento(request):
    return render(request, 'evento.html')


@login_required(login_url='/login/')
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        descricao = request.POST.get('descricao')
        data_evento = request.POST.get('data_evento')+" "+request.POST.get('hora_evento')
        usuario = request.user
        Evento.objects.create(
            titulo=titulo,
            data_evento=data_evento,
            descricao=descricao,
            usuario=usuario
        )
    return redirect('/')

def login_user(request):
    return render(request, "login.html")


def submit_login(request):
    if request.POST:
        nome = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = authenticate(username=nome, password=senha)
        print(usuario)
        if usuario:
            login(request, usuario)

        else:
            messages.error(request, "Usuario ou Senha Invalidos")  #  retorna em caso da autenticação falhar
    return redirect('/')


def logout_user(request):
    logout(request)
    return redirect('/')


def index(request):
    return redirect('/agenda/')
