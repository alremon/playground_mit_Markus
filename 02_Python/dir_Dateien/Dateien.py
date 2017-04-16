#!/usr/local/bin/python

# Datei einlesen

dateinamen_read = input ("Geben Sie die Datei an, die eingelesen werden soll: ")

#dateihandler_read = open ("Namen.txt")
dateihandler_read = open (dateinamen_read)

dateiinhalt_read = dateihandler_read.read()

print (dateiinhalt_read)

liste_woerter = dateiinhalt_read.split(" " and "\n")
print (liste_woerter)
print ("Die Datei hat "+str(len(liste_woerter))+" Woerter!")

exit()

# Datei schreiben

dateinamen_write = input ("Geben Sie den Namen der Datei an, in die der Text geschrieben werden soll: ")

dateihandler_write = open (dateinamen_write,mode="a")
#dateihandler_write = open ("Datei_schreiben.txt",mode="a")

liste = [1,3,5,2,6,4,7]

for element in liste:
	dateihandler_write.write(str(element))
	dateihandler_write.write("\n")
	print (element)
	

#irgendeinstring = "Hier steht irgendwas\nUnd das müsste eine neue Zeile sein"

#dateiinhalt_write = irgendeinstring
#dateiinhalt_write = str(liste)


#	print (dateiinhalt_write)
