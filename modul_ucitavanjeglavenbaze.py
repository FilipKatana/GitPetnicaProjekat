import csv
from fakemodul_fajl import *
import itertools
import sys


class glavnaBaza:
    
    def __init__ (self, _fajl , fajlovi = { "" : "" } ):
        self._fajl = _fajl
        self.fajlovi = fajlovi
        self.fajlovi [_fajl.path] = _fajl.ime
        
    #Molim te dodaj funkciju za učitavanje iz baze.
        
    def pisiUCSV(self):
        f = open("glavnabaza.csv" , "a")
        for key in self.fajlovi.keys():
            f.write(str(key) + "," + str(self.fajlovi[key]) + "\n")
        
    """
    def dodajFolderuIliFajlUBazu(fajl):
        path = fajl.path
        if self.fajlovi[path] not {}:
            self.fajlovi[path] = fajl
        else:
            self.fajlovi
    """   
        

flt = open('fajl2' , "r")
fl = fajl(flt )
gl = glavnaBaza(fl).pisiUCSV()


    
