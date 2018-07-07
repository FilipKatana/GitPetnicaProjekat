keyword = ["commit" , "add" , "init"]

from modul_intrepreter import *
from modul_commit import *
from modul_init import *

print("intrprint")
strInput = input()


if strInput == "init":
    inicijalizacija()

else if strInput == "commit":
    commit("fajl" , "desc" , "v1")

else:
    print("Incorect syntax")
