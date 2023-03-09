from django.db import models

# Create your models here.
class imovel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    endereco = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    numero_quartos = models.IntegerField()
    numero_banheiros = models.IntegerField()
    numero_vagas = models.IntegerField()
    disponivel = models.BooleanField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_alteracao = models.DateTimeField(auto_now=True)
    imagem = models.ImageField(upload_to='imoveis', blank=True, null=True)
    def __str__(self):
        return self.nome