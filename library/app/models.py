from django.db import models
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=100)
    auteur = models.CharField(max_length=100)
    categorie=models.CharField(max_length=100)
    disponibilite=models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)  # Changer "Date" en "date"
    isbn = models.CharField(max_length=100,default=True)  # Changer "ISBN" en "isbn"
    resume = models.CharField(max_length=100,default=True)  # Changer "Resume" en "resume"

    def __str__(self):
        return self.title

