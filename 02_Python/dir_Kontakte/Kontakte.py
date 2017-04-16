#!/usr/local/bin/python

class Kontakt:
	def __init__(self,name,vorname,telefon):
		self.myName = name
		self.myVorname = vorname
		self.myTelefon = telefon
		print ("Kontakt erstellt!")	

	def printKontakt(self):
		print ("Der Kontakt hat den Namen "+self.myName+", den Vornamen "+self.myVorname+" und die Telefonnummer "+self.myTelefon+".") 

kontakt_001 = Kontakt("Remon","Alexandre","017681119798")

kontakt_001.printKontakt()

print ("Hallo Klasse!")
