#  hello/views.py

import datetime
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Portfolio, PontuacaoQuizz
from .forms import PortfolioForm


def home_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'home.html', context)


def about_page_view(request):
    agora = datetime.datetime.now()
    local = 'Lisboa'
    topicos = ['HTML', 'CSS', 'Python', 'Django', 'JavaScript']

    context = {
        'hora': agora.hour,
        'local': local,
        'topicos': topicos,
    }
    return render(request, 'about.html', context)


def web_page_view(request):
    return render(request, 'web.html')

def contactos_page_view(request):
    return render(request, 'contactos.html')


def projetos_page_view(request):
    return render(request, 'projetos.html')


def hero_page_view(request):
    return render(request, 'hero.html')


def blog_page_view(request):
    context = {'comentarios': Portfolio.objects.all()}
    return render(request, 'blog.html', context)


def novo_comentario_view(request):
    form = PortfolioForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))
    context = {'form': form}
    return render(request, 'novo.html', context)


def edita_comentario_view(request, comentario_id):
    comentario = Portfolio.objects.get(id=comentario_id)
    form = PortfolioForm(request.POST or None, instance=comentario)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('portfolio:blog'))

    context = {'form': form, 'comentario_id': comentario_id}
    return render(request, 'edita.html', context)


def apaga_comentario_view(request, comentario_id):
    Portfolio.objects.get(id=comentario_id).delete()
    return HttpResponseRedirect(reverse('projeto:blog'))


def pontuacao_quizz(request):
    return request.pontuacao


def quizz(request):
    if request.method == 'POST':
        n = request.POST['nome']
        p = pontuacao_quizz(request)
        r = PontuacaoQuizz(nome=n, pontuacao=p)
        r.save()
    return render(request, 'quizz.html')