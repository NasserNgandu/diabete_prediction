from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from Administrateur.models import Administrateur
from Patient.models import Patient
from Test.models import Test
import requests

#Prediction
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd

def login(request):
	if request.method == "POST":
		# recuperation des informations de connexion
		username = request.POST.get("username", None)
		password = request.POST.get("userpassword", None)

		if username and password:
			try:
				administrateur = Administrateur.objects.get(Login=username, Pwd=password)
			except Administrateur.DoesNotExist as e:
				return render(request, "connexion.html", {"connexion": "no"})
			else:
				# creation de la session
				session_administrateur = {"id_administrateur":administrateur.id,
					"nom":administrateur.Nom,
					"postnom":administrateur.PostNom,
					"prenom":administrateur.Prenom,
					"login":administrateur.Login,
				}
				request.session["session_administrateur"] = session_administrateur
			return redirect(accueil)
	return render(request, "connexion.html")

def accueil(request):
	patients = Patient.objects.all()
	list_patients = []

	total_test = len(patients)
	total_test_positif = 0
	total_test_negatif = 0
	total_test_prediabete = 0

	for patient in patients:
		if int(patient.Test.Diabetes_012) == 0:
			resultat = "Negatif"
			total_test_negatif += 1
		elif int(patient.Test.Diabetes_012) == 1:
			 resultat = "Prediabete"
			 total_test_prediabete += 1
		elif int(patient.Test.Diabetes_012) == 2:
			 resultat = "Diabete"
			 total_test_positif += 1
		list_patients.append(
			{
				'id' : patient.id,
				'nom' : patient.Nom,
				'postnom' : patient.PostNom,
				'prenom' : patient.Prenom,
				'date_naissance' : patient.DateNaissance,
				'resultat' : resultat,
			}
		)
	if total_test_positif > 0:
		total_test_positif_pourc = total_test_positif / total_test  * 100
	else:
		total_test_positif_pourc = 0
	if total_test_negatif > 0:
		total_test_negatif_pourc = total_test_negatif / total_test * 100
	else:
		total_test_negatif_pourc = 0
	if total_test_prediabete > 0:
		total_test_prediabete_pourc = total_test_prediabete / total_test * 100
	else:
		total_test_prediabete_pourc = 0

	return render(request, "accueil.html", locals())

def prediction(request):
	if request.method == "POST":
		Nom = request.POST.get("Nom", None)
		PostNom = request.POST.get("PostNom", None)
		Prenom = request.POST.get("Prenom", None)
		DateNaissance = request.POST.get("DateNaissance", None)

		Age = 10
		HighBP = request.POST.get("HighBP", None)
		HighChol = request.POST.get("HighChol", None)
		CholCheck = request.POST.get("CholCheck", None)
		BMI = request.POST.get("BMI", None)
		Smoke = request.POST.get("Smoke", None)
		Stroke = request.POST.get("Stroke", None)
		HeartDiseaseorAttak = request.POST.get("HeartDiseaseorAttak", None)
		PhysicActivity = request.POST.get("PhysicActivity", None)
		Fruits = request.POST.get("Fruits", None)
		Veggies = request.POST.get("Veggies", None)
		Sex = request.POST.get("Veggies", None)
		Algorithme = request.POST.get("Algorithme", None)

		try:
			if Algorithme == "1":
				#KNN
				requete = requests.get("http://127.0.0.1:5000/prediction/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s" %(HighBP,
					HighChol, CholCheck, BMI, Smoke, Stroke, HeartDiseaseorAttak, PhysicActivity, Fruits, Veggies, Sex, Age))
			else:
				#Naive Bayes
				requete = requests.get("http://127.0.0.1:6000/prediction/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s/%s" %(HighBP,
					HighChol, CholCheck, BMI, Smoke, Stroke, HeartDiseaseorAttak, PhysicActivity, Fruits, Veggies, Sex, Age))

			Diabetes_012 = float(requete.json()['resultat'])
			test = Test(
				HighBP = HighBP,
				HighChol = HighChol,
				CholCheck = CholCheck,
				BMI = BMI,
				Smoke = Smoke,
				Stroke = Stroke,
				HeartDiseaseorAttak = HeartDiseaseorAttak,
				PhysicActivity = PhysicActivity,
				Fruits = Fruits,
				Diabetes_012 = Diabetes_012,
				Sex = Sex,
				Veggies = Veggies,
				Age = Age,
				)
			test.save()
			patient = Patient(
				Nom = Nom,
				PostNom = PostNom,
				Prenom = Prenom,
				DateNaissance = DateNaissance,
				Test = test,
				)
			patient.save()
		except :
			print("Une erreur s'est produite")
	
	return redirect(accueil)