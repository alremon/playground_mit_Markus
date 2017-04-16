#!/usr/local/bin/python

# Ganze Zahlen

ganzeZahl = 5

print (ganzeZahl)

#type(ganzeZahl)

print (type(ganzeZahl))


# Fliesszahlen

fliessZahl = 1.35

print (fliessZahl)

print (type(fliessZahl))


# String - Zeichenkette

zeichenkette = "Hier steht ein Satz!"

print (zeichenkette)
print (type(zeichenkette))


# Boolean

wahrfalsch = True

print (wahrfalsch)
print (type(wahrfalsch))


# Liste/Array

liste = [41,72,-3,24,-65]

print (liste) 
print (type(liste)) 



# MIN/MAX-Funktion einer Liste

bisherGroessteZahl = liste[0]
bisherKleinsteZahl = liste[0]

for element in liste:
	if element > bisherGroessteZahl:
		bisherGroessteZahl = element
	if element < bisherKleinsteZahl:
		bisherKleinsteZahl = element
	
	
print ("Bisher groesste Zahl: "+str(bisherGroessteZahl))
print ("Bisher kleinste Zahl: "+str(bisherKleinsteZahl))
		
