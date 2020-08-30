from django.db import models

class Person(models.Model):
    nome = models.CharField(max_length=30)
    sobrenome = models.CharField(max_length=30)
    apelido = models.CharField(max_length=30, null=True, blank=True)
    data_nascimento = models.IntegerField()
    email = models.CharField(max_length=30)
    idade = models.IntegerField()
    observacao = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)

    def __str__(self):
        return self.nome + ' ' + self.sobrenome
