luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))
valinta1 = luku1 + luku2
print("(1) +")
valinta2 = luku1 - luku2
print("(2) -")
valinta3 = luku1 * luku2
print("(3) *")
valinta4 = luku1 / luku2
print("(4) /")

valinta = input("Tee valinta (1-4): ")
if valinta == "1":
    tulos=valinta1
elif valinta == "2":
    tulos=valinta2
elif valinta == "3":
    tulos=valinta3
elif valinta =="4":
    tulos=valinta4
else:
    print("Valintaa ei tunnistettu.")
    tulos = None

if tulos is not None:
    print("Tulos on:", tulos)