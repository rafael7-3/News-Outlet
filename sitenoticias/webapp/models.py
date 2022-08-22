from django.db import models
from django.contrib.auth.models import User
# Create your models here.

  
class Noticia(models.Model):
    editor = models.CharField(max_length = 150)
    titulo = models.CharField(max_length = 180)
    texto = models.CharField(max_length = 9000)
    imagem = models.ImageField(upload_to='media', null=True, blank=True)
    

class Comentario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE) 
    texto = models.CharField(max_length = 500) 