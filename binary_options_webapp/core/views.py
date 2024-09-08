from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    context = {}
    return HttpResponse(template.render(context, request))


def bet(request):
    template = loader.get_template("bet.html")
    context = {}
    return HttpResponse(template.render(context, request))


def transaction_history(request):
    template = loader.get_template("transaction_history.html")
    context = {}
    return HttpResponse(template.render(context, request))


def deposit(request):
    template = loader.get_template("deposit.html")
    context = {}
    return HttpResponse(template.render(context, request))


def sell(request):
    template = loader.get_template("sell.html")
    context = {}
    return HttpResponse(template.render(context, request))


def profile(request):
    template = loader.get_template("profile.html")
    context = {}
    return HttpResponse(template.render(context, request))
