# Dieses Skript soll die Bilder und Videos eines Ordners in Ordner des jeweiligen Datums (Änderungsdatum) verschieben

#import ctypes
import os
#import time
import _datetime
import shutil

#print ("Hello World")

# Pfad angeben, wo Bilder enthalten sind
pfad = input ("Bitte den Pfad angeben, wo die Bilder enthalten sind, die in Datums-Ordner einsortiert werden sollen: ")
#pfad = "C:\\Test"
#datei = "001.jpg"

# Liste erstellen mit allen JPG, jpg, MOV, mp4 Dateien des angegebenen Ordners

liste_aller_Dateien_des_pfads = os.listdir(pfad)
print (liste_aller_Dateien_des_pfads)

# Schleife über alle Dateien
for datei in liste_aller_Dateien_des_pfads:

    Dateipfad = (pfad + "\\" + datei)

    print(Dateipfad)
    #print(os.path.exists(Dateipfad))

    # Dateiendung extrahieren
    Dateipfad_splitted_mit_Punkt = Dateipfad.split(sep=".")
    Dateiendung = Dateipfad_splitted_mit_Punkt[-1]

    if (Dateiendung == "jpg" or Dateiendung == "JPG" or Dateiendung == "MOV" or Dateiendung == "mov" or Dateiendung == "mp4" or Dateiendung == "png" or Dateiendung == "PNG"):

        Aenderungsdatum_in_sekunden = os.path.getmtime(Dateipfad)
        Aenderungsdatum_komplett = _datetime.datetime.utcfromtimestamp(Aenderungsdatum_in_sekunden)
        print(Aenderungsdatum_komplett)

        # konvertierung zu String
        Aenderungsdatum_komplett_str = str(Aenderungsdatum_komplett)

        # Abspalten des Datums von der Zeit
        Aenderungsdatum_gesplittet = Aenderungsdatum_komplett_str.split()
        Aenderungsdatum_nur_Datum = Aenderungsdatum_gesplittet[0]

        # Erstellen des Datumpfads
        Datumspfad = pfad + "\\" + Aenderungsdatum_nur_Datum + "_"

        if str(os.path.exists(Datumspfad)) == "True":
            #print ("Ordner existiert bereits!")
            print ("")
        else:
            os.mkdir(Datumspfad)
            #print ("Ordner " + Datumspfad + " wird erstellt")

        # Datei in Ordner verschieben

        source = Dateipfad
        destiny = Datumspfad + "\\" + datei

        shutil.move(source,destiny)
