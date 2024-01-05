from django.db import models

class Administrateur(models.Model):
	Nom = models.CharField(max_length=100)
	PostNom = models.CharField(max_length=100)
	Prenom = models.CharField(max_length=100)
	Login = models.CharField(max_length=100)
	Pwd = models.CharField(max_length=100)

	def __str__(self):
		return "%s %s %s"%(self.Nom, self.PostNom, self.Prenom)
