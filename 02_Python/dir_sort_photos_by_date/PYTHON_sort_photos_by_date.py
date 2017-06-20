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

# Liste erstellen mit allen JPG, jpg, MOV, mp4, NEF Dateien des angegebenen Ordners

liste_aller_Dateien_des_pfads = os.listdir(pfad)

# Schleife über alle Dateien
for datei in liste_aller_Dateien_des_pfads:

    Dateipfad = (pfad + "\\" + datei)
    print(Dateipfad)

    # Dateiendung extrahieren
    Dateipfad_splitted_mit_Punkt = Dateipfad.split(sep=".")
    Dateiendung = Dateipfad_splitted_mit_Punkt[-1]

    if (Dateiendung == "jpg" or Dateiendung == "JPG" or Dateiendung == "jpeg" or Dateiendung == "JPEG" or Dateiendung == "MOV" or Dateiendung == "mov" or Dateiendung == "mp4" or Dateiendung == "png" or Dateiendung == "PNG" or Dateiendung == "NEF" or Dateiendung == "nef"or Dateiendung == "WAV" or Dateiendung == "wav" or Dateiendung == "mp3" or Dateiendung == "opus"):

        Dateidatum_nur_Datum = ""

        # Extrahierung des Aufnahmedatum
        file = open(Dateipfad, 'rb')
        tags_in_file = exifread.process_file(file)
        for tag_in_file in tags_in_file.keys():
            if (tag_in_file == "EXIF DateTimeOriginal"):
                Datum_aus_EXIF = (tags_in_file[tag_in_file])
                Dateidatum_nur_Datum = extrahiere_Datum_EXIF(Datum_aus_EXIF)
        file.close()

        # Extrahierung des Aenderungsdatums, falls kein Aufnahmedatum gefunden
        if (Dateidatum_nur_Datum == ""):
            # Aenderungsdatum
            Dateidatum_in_sekunden = os.path.getmtime(Dateipfad)
            Dateidatum_nur_Datum = extrahiere_Datum(Dateidatum_in_sekunden)

        # Verschiebung der Datei in den Ordner, falls Datum gefunden
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
