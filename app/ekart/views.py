from django.shortcuts import render
from .models import Mobile, Toys


def index(request):
    # mobile = Mobile()
    return render (request, 'pogo.html')


def detail(request, id):
    mobile = Mobile.objects.get(pk=id)
    return render(request, 'detail.html', {'mobile':mobile})


def more(request, id):
    toys = Toys.objects.get(pk=id)
    return render(request, 'more.html', {'toys':toys})


def index1(request):
    all_mobile = Mobile.objects.all()
    return render(request, 'index1.html',{'all_mobile':all_mobile})


def index2(request):
    all_toys = Toys.objects.all()
    return render(request, 'index2.html',{'all_toys':all_toys})