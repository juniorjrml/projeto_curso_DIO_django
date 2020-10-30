from django.shortcuts import render, HttpResponse

def hello(request, nome, idade):
    return HttpResponse('Hello Word {}! Voce tem {} anos!'.format(nome, idade))
