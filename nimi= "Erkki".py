nimi= "Erkki"
salasana= "Esimerkki"
inputnimi = input("Anna nimi: ")
inputsalasana = input("Anna salasana: ")

if inputnimi == nimi:
    print("Nimi oli oikein!")
    if inputsalasana == salasana:
        print("Salasana oli oikein!")
        print("Salasana ja nimi oli oikein")
    else:
        print("Salasana oli väärin!")
else:
    print("Nimi oli väärin!")
