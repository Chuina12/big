from tabnanny import verbose
from django.db import models

# Create your models here.

class Article(models.Model):
    titre = models.CharField(max_length=200)
    slogan = models.CharField(max_length=200)
    texte =models.TextField()
    photo = models.FileField()
    
    class Meta:
        verbose_name=('Articles')
        verbose_name_plural =('Articles')
        
        def __st__(self):
            return self.titre 
        
        
class Abonnement(models.Model):
    email = models.EmailField()
    pays = models.CharField(max_length=20)