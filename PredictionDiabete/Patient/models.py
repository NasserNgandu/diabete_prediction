from django.db import models
from Test.models import Test

class Patient(models.Model):
	Nom = models.CharField(max_length=100)
	PostNom = models.CharField(max_length=100)
	Prenom = models.CharField(max_length=100)
	DateNaissance = models.DateField()
	Test = models.ForeignKey(Test, on_delete=models.CASCADE)

	def __str__(self):
		return "%s %s %s"%(self.Nom, self.PostNom, self.Prenom)
