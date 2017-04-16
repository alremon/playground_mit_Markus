#!/usr/local/bin/python

# WHILE-Schleife

i = 0

while i < 5:
	print (i)
	i = i + 1

print ()
print ()

# FOR-Schleife

liste = [7,6,5,4,3]

summe = 0

for element in liste:
	summe = summe + element
	print ("Die aktuelle Summe lautet "+str(summe))
	print (element)

print ()
print ()
