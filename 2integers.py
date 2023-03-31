luku1 = int(input("Anna luku: "))
luku2 = int(input("Anna toinen luku: "))

if luku1 % 2==0 and luku2 % 2==0:
	print("Molemmat luvut ovat parillisia")
elif luku1 %2==1 and luku2 % 2==1:
	print("Molemmat luvut ovat parittomia")
else:
	print("Toinen luku on parillinen")