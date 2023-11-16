from django.shortcuts import render
from .models import Dogs
from .models import Cats
from .models import Carousel


# Create your views here.

def index(request):
    carousel = Carousel.objects.all()
    return render(request, 'main/index.html', {'title': 'Главная страница', 'carousel': carousel})


def cats(request):
    cats = Cats.objects.all()
    return render(request, 'main/cats.html', {'cats': cats, 'title': 'Кошки'})


def dogs(request):
    dogs = Dogs.objects.all()
    return render(request, 'main/dogs.html', {'dogs': dogs, 'title': 'Собаки'})


def contacts(request):
    return render(request, 'main/contacts.html', {'title': 'Контакты'})


def how2Help(request):
    return render(request, 'main/how2Help.html', {'title': 'Как помочь'})


def tr_handler403(request, exeption):
    return render(request=request, template_name='main/error/403.html', status=403)


def tr_handler404(request, exception):
    return render(request=request, template_name='main/error/404.html', status=404)


def tr_handler500(request):
    return render(request=request, template_name='main/error/500.html', status=500)
