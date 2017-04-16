#!/usr/local/bin/python

class Rechteck:
	def __init__(self,laenge,breite):
		self.myLaenge = laenge
		self.myBreite = breite
		
		print ("Rechteck erstellt!")

	def printRechteck(self):
		print ("Das Rechteck hat eine Laenge von "+str(self.myLaenge)+" und eine Breite von "+str(self.myBreite)) 

	def calcUmfang(self):
		return 2*self.myBreite+2*self.myLaenge

	def calcFlaeche(self):
		return self.myBreite*self.myLaenge	

	def hatgroessereFlaeche(self,beliebiges_rechteck):
		selfFlaeche = self.calcFlaeche()
		beliebiges_rechteckFlaeche = beliebiges_rechteck.calcFlaeche()
		return selfFlaeche > beliebiges_rechteckFlaeche

rechteck1 = Rechteck(5,10)
rechteck2 = Rechteck(1,10)

rechteck1.printRechteck()
rechteck2.printRechteck()

print (rechteck1.calcFlaeche())
#rechteck2.calcFlaeche()

if rechteck1.hatgroessereFlaeche(rechteck2):
	print ("Rechteck 1 ist groesser")
else:
	print ("Rechteck 1 ist kleiner oder gleich gross")
