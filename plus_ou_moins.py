#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
# Jeu "PLUS OU MOINS" - Version 1.1
from random import randint

nombreADeviner = randint(30,100)
nombreJoueur = 0
while nombreJoueur!=nombreADeviner : #Le jeu tourne tant que le joueur a choisi un nombre different du juste prix

	nombreJoueur = int(input("Essayez de deviner le nombre entre 30 et 100 : "))

	if nombreJoueur<30 or nombreJoueur>100 :
		print("Il faut choisir un nombre entre 30 et 100.")
	elif nombreJoueur < nombreADeviner :
		print("Ce n'est pas le bon nombre, essayez plus grand.")
	elif nombreJoueur > nombreADeviner :
		print("Ce n'est pas le bon nombre, essayez plus petit.")
	else :
		print("Bravo, vous avez trouvé le juste prix. On vous offre un sejour à Paris.")

