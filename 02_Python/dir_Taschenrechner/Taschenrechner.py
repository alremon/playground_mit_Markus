#!/usr/local/bin/python

import sys

# Definition der Rechenfunktionen

# Addition
def addiere:
	


# Eingabe des Benutzers

print ()
print ("Dies ist ein Taschenrechner, der zwei beliebige Zahlen miteinander verrechnet.")
print ("1: Addition +")
print ("2: Subtraktion -")
print ("3: Multiplikaiton *")
print ("4: Division/Bruch /")
print ("5: Potenz **")
print ("6: Division mit Rest %")
print ("7: Fakultaet !")
print ()
rechenform = input ("Geben Sie an welche Rechenform verwendet werden soll (Zahl zw. 1-7): ")

try:
	rechenform_id = int(rechenform)
except:
	print (str(rechenform)+" ist keine (ganze) Zahl. Das Programm wird abgebrochen")
	exit()

print ("\n")

if rechenform_id < 7 and rechenform_id > 0:
	eingabe1 = int(input ("Bitte geben Sie die erste Zahl ein: "))
	eingabe2 = int(input ("Bitte geben Sie die zweite Zahl ein: "))

	# Addition
	if rechenform_id == 1:
		print ("=== Addition ===")
		ergebnis = eingabe1 + eingabe2
		print ("Das Ergebnis lautet "+str(ergebnis)+".")
	
	# Subtraktion
	elif rechenform_id == 2:
		print ("=== Subtraktion ===")
		ergebnis = eingabe1 - eingabe2
		print ("Das Ergebnis lautet "+str(ergebnis)+".")
	
	
	# Multiplikation	
	elif rechenform_id == 3:
		print ("=== Multiplikation ===")
		ergebnis = eingabe1 * eingabe2
		print ("Das Ergebnis lautet "+str(ergebnis)+".")
	
	
	# Division
	elif rechenform_id == 4:
		print ("=== Division ===")
		ergebnis = eingabe1 / eingabe2
		print ("Das Ergebnis lautet "+str(ergebnis)+".")
	
	
	# Potenz
	elif rechenform_id == 5:
		print ("=== Potenz ===")
		ergebnis = eingabe1 ** eingabe2
		print ("Das Ergebnis lautet "+str(ergebnis)+".")
	
	
	# Division mit Rest
	elif rechenform_id == 6:
		print ("=== Division mit Rest ===")
		ergebnis = eingabe1 // eingabe2
#		ergebnis = int(eingabe1 / eingabe2)
		ergebnisRest = eingabe1 % eingabe2
		print ("Das Ergebnis lautet "+str(ergebnis)+" mit einem Rest von "+str(ergebnisRest)+".")


elif rechenform_id == 7:
	eingabe1 = int(input ("Bitte geben Sie die (ganze) Zahl an deren Fakultaet berechnet werden soll: "))
	print ("=== Fakultaet ===")
	eingabe1Temp = eingabe1
	ergebnis = 1
	while eingabe1Temp > 1:
		ergebnis = ergebnis * eingabe1Temp
		eingabe1Temp = eingabe1Temp - 1
	print ("Das Ergebnis für die Falkutaet von "+str(eingabe1)+" ist "+str(ergebnis)+".")

else:
	print ("Es wurde keine Zahl von 1-7 angegeben. Das Programm wird beendet.")
	exit ()
	


print ()
