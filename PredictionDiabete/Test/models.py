from django.db import models

class Test(models.Model):
	#Pression Arterielle
	HighBP = models.BooleanField()
	#Hypercholesterolemie : Niveeau eleve du chloresterol
	HighChol = models.BooleanField()
	#Verification du chloresterol dans les 5 dernieres annees
	CholCheck = models.BooleanField()
	#Indice de masse corporelle
	BMI = models.FloatField()
	#Fume au moins 100 cigarette dans la vie(100 cigarettes = 5 paquets)
	Smoke = models.BooleanField()
	#AVC : accident vasculaire cérébral
	Stroke = models.BooleanField()
	#Crise cardiaque
	HeartDiseaseorAttak = models.BooleanField()
	#Activite physique dans le 30 derniers jours travail non inclus
	PhysicActivity = models.BooleanField()
	#Consommation des fruits au moins une fois le jours
	Fruits = models.BooleanField()
	#Age
	Age = models.FloatField()
	#Sexe
	Sex = models.BooleanField()
	#Vegetarien
	Veggies = models.BooleanField()
	"""
	Resultat Test
	0 : Pas de diabete ou seulement pendans la grossesse
	1 : Prediabete
	2 : Diabete
	""" 
	Diabetes_012 = models.FloatField()

	def __str__(self):
		return "%s"%(self.Diabetes_012)