class fajl:
    def __init__(self , path = "usrmnt" , fajl = open("fajl" , "r") , trenutnaverzija = "1" , trenutnaverzijausr = "1",message = "komit",adovan = True):
        self.path = path
        self.fajl = fajl
        self.trenutnaverzija = trenutnaverzija
        self.trenutnaverzijausr = trenutnaverzijausr
        self.message = message
        self.adovan = adovan