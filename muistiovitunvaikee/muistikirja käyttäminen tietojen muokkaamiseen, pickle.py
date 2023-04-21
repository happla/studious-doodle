import os.path
import time
import pickle

memo_file = "muistio.dat"

if not os.path.isfile("muistio.dat"):
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    with open(memo_file, "wb") as f:
        pickle.dump([], f)

with open(memo_file, "rb") as f:
    muistio = pickle.load(f)

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja lopeta")
    userInput = int(input("Mitä haluat tehdä?: "))
    if userInput == 1:
        entry = muistio[0]
        print(f"{entry['text']}:::{entry['timestamp']}")

    elif userInput == 2:
        userInput = input("Kirjoita uusi merkintä: ")
        timestamp = time.strftime("%X %x")
        muistio.append({"text": userInput, "timestamp": timestamp})

    elif userInput == 3:
        print(f"Listalla on {len(muistio)} merkintää.")
        userInput = int(input("Mitä niistä muutetaan?: "))
        if userInput == 1:
            entry = muistio[0]
            print(f"{entry['text']} ::: {entry['timestamp']}")
            new_text = input("Anna uusi teksti: ")
            timestamp = time.strftime("%X %x")
            muistio[0] = {"text": new_text, "timestamp": timestamp}
        elif userInput < len(muistio):
            entry = muistio[userInput]
            print(f"{entry['text']} ::: {entry['timestamp']}")
            new_text = input("Anna uusi teksti: ")
            timestamp = time.strftime("%X %x")
            muistio[userInput] = {"text": new_text, "timestamp": timestamp}
        else:
            print("Virheellinen valinta.")

    elif userInput == 4:
        print(f"Listalla on {len(muistio)} merkintää.")
        userInput = int(input("Mitä niistä poistetaan?: "))
        if userInput <= len(muistio) and userInput > 0:
            removed_entry = muistio.pop(userInput - 1)
            print(f"Poistettiin merkintä {removed_entry['text']}:::{removed_entry['timestamp']}")
        else:
            print("Virheellinen valinta.")

    elif userInput == 5:
        with open(memo_file, "wb") as f:
            muistio_strings = [f"{entry['text']}:::{entry['timestamp']}" for entry in muistio]
            pickle.dump(muistio_strings, f)
        print("Lopetetaan.")
        break
