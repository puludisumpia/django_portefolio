from django.db import models
from fontawesome_5.fields import IconField

class Project(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to="images/portefolio/")
    note = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    modal_id = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Technologie(models.Model):
    name = models.CharField(max_length=100)
    icon = IconField()
    note = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField("Votre Nom".upper(), max_length=100)
    email = models.EmailField("Votre Mail".upper(), max_length=100)
    content = models.TextField("Votre Message".upper())
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    


