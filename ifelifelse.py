valinta1="Haukion kala Oy"
valinta2="Metallipaja VasaraAika"
valinta3="Balin palapelitehdas"

valinta=input("Valitse kohde(1-3): ")
valinta=int(valinta)
if valinta == 3:
	print(valinta3)
elif valinta == 2:
	print(valinta2)
else:
	print(valinta1)