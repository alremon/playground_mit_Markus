#!/usr/local/bin/python

# Zufallsgenerator (fuer pseudozufaellige Zahlen)

# Import der Funktion "randint" aus der Bibliothek "random"
from random import randint

liste = []

AnzahlDerElemente = 1000

i = 0

while AnzahlDerElemente > i:
	hinzu = randint (1,100000) # Parameterliste durch Komma getrennt
	liste.append(hinzu) # Liste mit Variablenwert aus hinzu erweitern
	i = i + 1

print (liste)

# Zufallsgenerator

bisherGroessteZahl = liste[0]
bisherKleinsteZahl = liste[0]

for element in liste:
	if element > bisherGroessteZahl:
		bisherGroessteZahl = element
	if element < bisherKleinsteZahl:
		bisherKleinsteZahl = element
	
	
print ("Bisher groesste Zahl: "+str(bisherGroessteZahl))
print ("Bisher kleinste Zahl: "+str(bisherKleinsteZahl))
		
