from django.shortcuts import render
from .models import Manutencao
# Create your views here.

def home(request):
    return render(request,'bancada/home.html')

def manutencoes(request):
    nova_manutencao = Manutencao()
    nova_manutencao.empresa = request.POST.get('empresa')
    nova_manutencao.tell = request.POST.get('tell')
    nova_manutencao.save()

    manutencoes = {
        'manutencoes': Manutencao.objects.all()
    }

    return render(request,'bancada/manutencoes.html',manutencoes)