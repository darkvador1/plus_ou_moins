#!/usr/bin/python3.4
# -*-coding:Utf-8 -*
# Jeu "PLUS OU MOINS" - Version 4.2
from random import randint

nombreADeviner = randint(30,100)
print("_PHASE_TEST_ nombreADeviner :",nombreADeviner) #Affichage uniquement en phase de test/debug
nombreDuJoueur = 0
nombreTentatives = 0
finPartie = False
gagne = False
while not(finPartie) : #Le jeu tourne tant que le joueur a choisi un nombre different du juste prix

	nombreDuJoueur = input("Essayez de deviner le nombre entre 30 et 100 : ")

	if nombreDuJoueur.isdigit() :              # On verfie que nombreDuJoueur est bien un nombre
		nombreDuJoueur = int(nombreDuJoueur) # Pour ensuite le convertir en un entier
		if nombreDuJoueur<30 or nombreDuJoueur>100 :
			print("Il faut choisir un nombre entre 30 et 100.")
		elif nombreDuJoueur < nombreADeviner :
			print("Ce n'est pas le bon nombre, essayez plus grand.")
			nombreTentatives = nombreTentatives + 1
		elif nombreDuJoueur > nombreADeviner :
			print("Ce n'est pas le bon nombre, essayez plus petit.")
			nombreTentatives = nombreTentatives + 1
		else :
			print("Bravo, vous avez trouvé le juste prix. On vous offre un sejour à Paris.")
			nombreTentatives = nombreTentatives + 1
			finPartie = True
			gagne = True
	else :
		print("Entrez un nombre entier !")

	if nombreTentatives>=5 and nombreTentatives!=10:
		print("Attention il ne vous reste plus que", 10-nombreTentatives,"tentatives.")
		print("Faites attention ou sinon vous ne gagnerez pas un voyage a Paris..."  )

	if nombreTentatives >= 10 :
		print("Vous avez atteint le maximum d'essais (10).")
		print("Le juste prix était :",nombreADeviner)
		finPartie = True

if gagne :
	print("Vous avez eu besoin de",nombreTentatives,"tentative(s).")
