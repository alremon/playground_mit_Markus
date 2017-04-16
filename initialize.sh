#!/bin/sh
if [ $PWD="/home/aremon/01_Programmierung" ]
	then
		PREFIX_PERL="/home/aremon/01_Programmierung/01_Perl"
		PREFIX_PYTHON="/home/aremon/01_Programmierung/02_Python"
fi
#echo $PREFIX
#echo $PWD
#echo $PREFIX_PERL
#echo $PREFIX_PYTHON

export PREFIX_PERL
export PREFIX_PYTHON
#export PREFIX

# Todo
# Per Shell herausfinden, in welchem Ordner die Perl-Skripte liegen
# Per Shell herausfinden, auf welchem Rechner man sich befindet
