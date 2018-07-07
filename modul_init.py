from fakemodul_fajl import *
import os

f = open("fajl")

nizAddovanihFajlova = [fajl(f)]

def inicijalizacija():
    try:
        if not os.path.exists("backup"):
            print("succes init")
            os.makedirs("backup")
    except OSError:
        print ('Error init ')
        return False





