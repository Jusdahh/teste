from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView, CreateView, UpdateView
from imoveis.models import imovel


class ImoveisView(ListView):
    model = imovel
    queryset = imovel.objects.all().order_by('nome')

class ImovelCreateView(CreateView):
    model = imovel
    fields = ['nome', 'descricao', 'endereco', 'preco', 'numero_quartos', 'numero_banheiros', 'numero_vagas', 'disponivel', 'imagem']
    success_url = '/imoveis/'

class ImovelUpdateView(UpdateView):
    model = imovel
    fields = ['nome', 'descricao', 'endereco', 'preco', 'numero_quartos', 'numero_banheiros', 'numero_vagas', 'disponivel', 'imagem']
    success_url = '/imoveis/'