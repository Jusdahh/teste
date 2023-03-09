from django import forms
from imoveis.models import imovel

class ImovelForm(forms.ModelForm):
    class Meta:
        model = imovel
        fields = ['nome', 'descricao', 'endereco', 'preco', 'numero_quartos', 'numero_banheiros', 'numero_vagas', 'disponivel', 'imagem']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields[imovel].queryset = imovel.objects.all()
        