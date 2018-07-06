import csv

class glavnaBaza:
    
    def __init__ ( fajl , fajlovi):
        fajl = fajl
        fajlovi = fajlovi

    def pisiUCSV():
        with open('glavnabaza.csv',"wb") as file:
            for line in self.fajlovi:
                file.write(line)
                file.write("\n")

    