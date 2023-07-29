from django.db import models

# Create your models here.


class Portfolio(models.Model):
    nome = models.CharField(max_length=100)
    comentario = models.CharField(max_length=600)
    criado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome[:50]


class PontuacaoQuizz(models.Model):
    nome = models.CharField(max_length=64)
    pontuacao = models.IntegerField(max_length=10)


class Linguagem(models.Model):
    nome = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.nome}"



class Professor(models.Model):
    nome = models.CharField(max_length=64)
    numero = models.IntegerField(max_length=10)

    def __str__(self):
        return f"{self.nome}({self.numero})"


class Projeto(models.Model):
    nome = models.CharField(max_length=64)


    def __str__(self):
        return f"{self.nome}({self.id})"


class Cadeira(models.Model):
   nome = models.CharField(max_length=20)
   ano = models.IntegerField()
   descricao = models.TextField()
   linguagens = models.ManyToManyField(Linguagem)
   docente_teorica = models.ForeignKey(Professor, on_delete=models.CASCADE)
   docentes_praticas = models.ManyToManyField(Professor, related_name='caderias')
   projetos = models.ManyToManyField(Projeto)
