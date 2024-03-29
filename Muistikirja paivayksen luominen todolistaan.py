import time

while True:
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Tyhjennä muistikirja")
    print("(4) Lopeta")

    userinput = input("Mitä haluat tehdä?: ")
    if userinput == "1":
        with open("muistio.txt", "r") as file:
            content = file.readlines()
            for line in content:
                print(line)
    elif userinput == "2":
        with open("muistio.txt", "a") as file:
            entry= input("Kirjoita uusi merkintä: ")
            timestamp = time.strftime("%x %X")
            file.write(f"{entry}:::{timestamp}\n")
    elif userinput == "3":
        with open("muistio.txt", "w") as file:
            print("Muistio tyhjennetty.")
    elif userinput == "4":
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")
