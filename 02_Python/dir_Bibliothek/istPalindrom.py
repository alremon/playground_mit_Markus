import sys

# Palindrom = Wort das von hinten wie von vorne dasselbe Wort ergeben
# anna = palindrom
# hans != palindrom
# lagerregal = palindrom

# es fehlt noch die

def istPalindrom (wort):
#	wort = wort.lower()
	wortlaenge = len(wort)
	istPalindrom = True
	i = 0
	
	while i < wortlaenge/2:
		
		if wort[i] != wort[wortlaenge - i - 1]:
			istPalindrom = False
			break
		i += 1
	
	return (istPalindrom)


while 1 == 1:
	eingabe = input("Bitte ein Wort eingeben, das ein Palindrom ist: ")
	if (istPalindrom(eingabe)==True):
		print ("Hat geklappt: das Wort \""+eingabe+"\" ist ein Palindrom gefunden!")
		break
	else:
		print ("Das Wort \""+eingabe+"\" ist kein Palindrom!")
