import csv
from fakemodul_fajl import fajl
import itertools

class glavnaBaza:
    
    def __init__ (self, file , fajlovi = {"podatak" : "fajl1"}):
        self.file = file
        self.fajlovi = fajlovi

    def pisiUCSV(self):
        f = open("glavnabaza.csv" , "w")
        
        for key in self.fajlovi.keys():
            f.write(str(key) + "," + str(self.fajlovi[key]) )
        
        


fl = fajl()
gl = glavnaBaza(fl).pisiUCSV()


    