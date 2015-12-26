#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
# Jeu "PLUS OU MOINS" - Version 2.2
from random import randint

nombreADeviner = randint(30,100)
print("_PHASE_TEST_ nombreADeviner :",nombreADeviner) #Affichage uniquement en phase de test/debug
nombreJoueur = 0
nombreTentatives = 0
while nombreJoueur!=nombreADeviner : #Le jeu tourne tant que le joueur a choisi un nombre different du juste prix

	nombreJoueur = input("Essayez de deviner le nombre entre 30 et 100 : ")

	if nombreJoueur.isdigit() :              # On verfie que nombreJoueur est bien un nombre
		nombreJoueur = int(nombreJoueur) # Pour ensuite le convertir en un entier
		if nombreJoueur<30 or nombreJoueur>100 :
			print("Il faut choisir un nombre entre 30 et 100.")
		elif nombreJoueur < nombreADeviner :
			print("Ce n'est pas le bon nombre, essayez plus grand.")
			nombreTentatives = nombreTentatives + 1
		elif nombreJoueur > nombreADeviner :
			print("Ce n'est pas le bon nombre, essayez plus petit.")
			nombreTentatives = nombreTentatives + 1
		else :
			print("Bravo, vous avez trouvé le juste prix. On vous offre un sejour à Paris.")
			nombreTentatives = nombreTentatives + 1
	else :
		print("Entrez un nombre entier !")
print("Vous avez eu besoin de",nombreTentatives,"tentative(s).")
