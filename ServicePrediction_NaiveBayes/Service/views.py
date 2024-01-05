from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
#Prediction
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd

#declaration de la variable global message
MODEL={
	"model" : "",
}

def creation_model(request, highBP, highChol, cholCheck, bMI, smoker, stroke, heartDiseaseorAttack, physActivity, fruits, veggies, sex, age):
	data_set = pd.read_csv('dataset/diabetes.csv')
	x = data_set[['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies','Sex','Age']]
	y = data_set['Diabetes_012']
	x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=0, test_size=.2)
	model = GaussianNB()
	model.fit(x_train, y_train) 
	model.score(x_test, y_test)
	MODEL["model"] = model
	return redirect(prediction, highBP, highChol, cholCheck, bMI, smoker, stroke, heartDiseaseorAttack, physActivity, fruits, veggies, sex, age)
@api_view(['GET'])
def prediction(request, highBP, highChol, cholCheck, bMI, smoker, stroke, heartDiseaseorAttack, physActivity, fruits, veggies, sex, age):
	reponse=dict()
	if request.method=='GET':
		"""
		controle du model
		"""
		if MODEL["model"] == "":
			return redirect(creation_model, highBP, highChol, cholCheck, bMI, smoker, stroke, heartDiseaseorAttack, physActivity, fruits, veggies, sex, age)
		prediction = MODEL["model"].predict([[float(highBP), float(highChol),
			float(cholCheck), float(bMI), 
			float(smoker), float(stroke),
			float(heartDiseaseorAttack), float(physActivity),
			float(fruits), float(veggies),
			float(sex), float(age)]])
		reponse['resultat'] = str(prediction[0])
		return Response(reponse)
