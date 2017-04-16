#!/usr/local/bin/python

import sys

wort = input ("Bitte das Wort eingeben, das geprueft werden soll, ob es ein Palindrom ist: ")

# anna = palindrom
# hans != palindrom
# lagerregal = palindrom

wortlaenge = len(wort)
istPalindrom = True
i = 0

while i < wortlaenge/2:
	
	if wort[i] != wort[wortlaenge - i - 1]:
		istPalindrom = False
		break
	i += 1

if istPalindrom == True:
	print ("Das Wort \""+wort+"\" ist ein Palindrom!")	
else:
	print ("Das Wort \""+wort+"\" ist kein Palindrom!")
