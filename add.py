def add(fileToAdd, listOfFilesToCommit):
    #Prima kao parametre objekat tipa file i listu fajlova koji se komituju
    #Dodaje fajl u listu fajlova koji ce da se komituju
    if fileToAdd not in listOfFilesToCommit:
        listOfFilesToCommit.append(fileToAdd)
    
