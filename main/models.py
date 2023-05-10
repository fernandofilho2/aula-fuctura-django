from django.db import models
from django.contrib.auth import get_user_model



class Aluno(models.Model):

    STATUS = (
        ('ativo','Ativo'),
        ('inativo', 'Inativo'),
    )   
    
    nome = models.CharField(max_length=255)
    telefone = models.CharField(null= True, blank=True, max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField(null=True)
    description = models.TextField()
    status = models.CharField(max_length=8, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True) #boas praticas
    updated_at = models.DateTimeField(auto_now=True) #boas praticas
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
class Cadastro(models.Model):
        
    email = models.EmailField()
    password = models.CharField(max_length=250)
    address = models.CharField(max_length=250)
    address2 = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    zip = models.CharField(max_length=250)

    def __str__(self):
        return self.email
    

