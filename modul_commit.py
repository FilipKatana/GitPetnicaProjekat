from fakemodul_fajl import *
import os

f = open("fajl")

nizAddovanihFajlova = [fajl(f)]

def commit(name , message , version):
    nasao = False
    for i in nizAddovanihFajlova :
        if i.ime == name:
            i.message = message
            i.trenutnaverzija += 1
            i.trenutnaverzijausr = version
            nasao = True
    if nasao == False:
        print("ne postoji taj fajl ili nije adovan")
    print(nizAddovanihFajlova[0].ime)


