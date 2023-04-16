import math

while True:
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))

    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5) sin(luku1/luku2)")
    print("(6) cos(luku1/luku2)")
    print("(7) Vaihda luvut")
    print("(8) Lopeta")
    print("Valitut luvut:", luku1, luku2)

    valinta = int(input("Tee valinta (1-8): "))

    if valinta == 1:
        tulos = luku1 + luku2
    elif valinta == 2:
        tulos = luku1 - luku2
    elif valinta == 3:
        tulos = luku1 * luku2
    elif valinta == 4:
        tulos = luku1 / luku2
    elif valinta == 5:
        tulos = math.sin(luku1/luku2)
    elif valinta == 6:
        tulos = math.cos(luku1/luku2)
    elif valinta == 7:
        continue
    elif valinta == 8:
        break
    else:
        print("Yritä uudelleen.")
        continue

    print("Tulos: ", tulos)
