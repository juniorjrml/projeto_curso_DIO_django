from django.shortcuts import render, HttpResponse
import math


def soma(request, a, b):
    return HttpResponse("O resultado de {} + {} é {}".format(a, b, a+b))


def subtracao(request, a, b):
    return HttpResponse("O resultado de {} - {} é {}".format(a, b, a-b))


def divisao(request, a, b):
    return HttpResponse("O resultado de {} / {} é {}".format(a, b, a/b))


def multiplicacao(request, a, b):
    return HttpResponse("O resultado de {} * {} é {}".format(a, b, a*b))
