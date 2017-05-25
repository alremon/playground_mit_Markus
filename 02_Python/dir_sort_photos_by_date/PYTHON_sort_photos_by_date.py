# Dieses Skript soll die Bilder und Videos eines Ordners in Ordner des jeweiligen Datums (Änderungsdatum) verschieben

#import ctypes
import os
#import time
import _datetime
import shutil
import exifread

def extrahiere_Datum (Datum_in_Sekunden_FUNKTION):
    Dateidatum_komplett = _datetime.datetime.utcfromtimestamp(Datum_in_Sekunden_FUNKTION)
    print(Dateidatum_komplett)
    # konvertierung zu String
    Dateidatum_komplett_str = str(Dateidatum_komplett)
    # Abspalten des Datums von der Zeit
    Dateidatum_gesplittet = Dateidatum_komplett_str.split()
    Dateidatum_nur_Datum_FUNKTION = Dateidatum_gesplittet[0]
    return Dateidatum_nur_Datum_FUNKTION

def extrahiere_Datum_EXIF (Datum_aus_EXIF_FUNKTION):
    # konvertierung zu String
    Dateidatum_komplett_str = str(Datum_aus_EXIF_FUNKTION)
    # Abspalten des Datums von der Zeit
    Dateidatum_gesplittet = Dateidatum_komplett_str.split()
    Dateidatum_nur_Datum_mit_Doppelpunkt = Dateidatum_gesplittet[0]
    Dateidatum_nur_Datum_FUNKTION = Dateidatum_nur_Datum_mit_Doppelpunkt.replace(':','-')
    return Dateidatum_nur_Datum_FUNKTION


# Pfad angeben, wo Bilder enthalten sind
pfad = input ("Bitte den Pfad angeben, wo die Bilder enthalten sind, die in Datums-Ordner einsortiert werden sollen: ")
#pfad = "C:\\Test"
#datei = "001.jpg"

# Datumsart
print ("Bitte geben Sie an nach welchem Datum sortiert werden soll: ")
print ("Datum (1)")
print ("Aufnahmedatum (2)")
print ("Änderungsdatum (3)")
print ("Erstellungsdatum (4)")
Datumsart = input ("Bitte geben Sie an nach welchem Datum sortiert werden soll (1,2,3 oder 4): ")

############# Abfangmechanismus einbauen, wenn der eingegebene Wert nicht 1,2,3,4 ist

# Liste erstellen mit allen JPG, jpg, MOV, mp4 Dateien des angegebenen Ordners

liste_aller_Dateien_des_pfads = os.listdir(pfad)
#print (liste_aller_Dateien_des_pfads)

# Schleife über alle Dateien
for datei in liste_aller_Dateien_des_pfads:

    Dateipfad = (pfad + "\\" + datei)

    print(Dateipfad)


    # Dateiendung extrahieren
    Dateipfad_splitted_mit_Punkt = Dateipfad.split(sep=".")
    Dateiendung = Dateipfad_splitted_mit_Punkt[-1]

    if (Dateiendung == "jpg" or Dateiendung == "JPG" or Dateiendung == "MOV" or Dateiendung == "mov" or Dateiendung == "mp4" or Dateiendung == "png" or Dateiendung == "PNG" or Dateiendung == "NEF" or Dateiendung == "nef"):

        Dateidatum_nur_Datum = ""

        if (Datumsart == "1"):
            # Datum
            Dateidatum_in_sekunden = os.path.getatime(Dateipfad)
            Dateidatum_nur_Datum = extrahiere_Datum(Dateidatum_in_sekunden)

        elif (Datumsart == "2"):
            file = open(Dateipfad, 'rb')
            tags_in_file = exifread.process_file(file)
            for tag_in_file in tags_in_file.keys():
                if (tag_in_file == "EXIF DateTimeOriginal"):
                    Datum_aus_EXIF = (tags_in_file[tag_in_file])
                    Dateidatum_nur_Datum = extrahiere_Datum_EXIF(Datum_aus_EXIF)
            file.close()

        elif (Datumsart == "3"):
            # Änderungsdatum
            Dateidatum_in_sekunden = os.path.getmtime(Dateipfad)
            Dateidatum_nur_Datum = extrahiere_Datum(Dateidatum_in_sekunden)

        elif (Datumsart == "4"):
            # Erstellungsdatum
            Dateidatum_in_sekunden = os.path.getctime(Dateipfad)
            Dateidatum_nur_Datum = extrahiere_Datum(Dateidatum_in_sekunden)

        if Dateidatum_nur_Datum != "":

            # Erstellen des Datumpfads
            Datumspfad = pfad + "\\" + Dateidatum_nur_Datum + "_"

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
