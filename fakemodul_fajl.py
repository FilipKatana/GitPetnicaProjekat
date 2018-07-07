import os

class fajl:
    def __init__(self , fajl, path = "" , ime = "" , trenutnaverzija = 1 , trenutnaverzijausr = "1" , message = "msg", adovan = True):
        self.fajl = fajl
        self.path = self.vratiPut()
        self.ime = self.vratiImeFajla()
        self.trenutnaverzija = trenutnaverzija
        self.trenutnaverzijausr = trenutnaverzijausr
        self.message = message
        self.adovan = adovan

    def vratiImeFajla (self):
        return self.fajl.name

    def vratiPut(self):
        return os.path.dirname(fajl.__name__)