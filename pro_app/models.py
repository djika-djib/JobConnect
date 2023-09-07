from django.db import models

# Create your models here.

class About(models.Model):
    # about_list = models.CharField(max_length=250)
    about_text = models.CharField(max_length=250)
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name
    

class Demande(models.Model):
    nom = models.CharField(max_length=256)
    prenom = models.CharField(max_length=256)
    email = models.EmailField()
    societe = models.CharField(max_length=256)
    message = models.TextField()
    def __str__(self):
        return self.nom + " " +self.prenom