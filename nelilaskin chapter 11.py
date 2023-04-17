import math

def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Virheellinen syöte!")

num1 = get_integer_input("Anna luku: ")
num2 = get_integer_input("Anna luku: ")

while True:
    print("(1) +")
    print("(2) -")
    print("(3) *")
    print("(4) /")
    print("(5)sin(luku1/luku2)")
    print("(6)cos(luku1/luku2)")
    print("(7)Vaihda luvut")
    print("(8)Lopeta")
    print("Valitut luvut:", num1 , num2)

    choice = get_integer_input("Tee valinta (1-8): ")

    if choice == 1:
        result = num1 + num2
        print("Tulos on: ", result)
    elif choice == 2:
        result = num1 - num2
        print("Tulos on: ", result)
    elif choice == 3:
        result = num1 * num2
        print("Tulos on: ", result)
    elif choice == 4:
        if num2 == 0:
            print("Virheellinen syöte! Et voi jakaa luvulla 0.")
        else:
            result = num1 / num2
            print("Tulos on: ", result)
    elif choice == 5:
        try:
            result = math.sin(num1 / num2)
            print("Tulos on: ", result)
        except ZeroDivisionError:
            print("Virheellinen syöte! Et voi jakaa luvulla 0.")
    elif choice == 6:
        try:
            result = math.cos(num1 / num2)
            print("Tulos on: ", result)
        except ZeroDivisionError:
            print("Virheellinen syöte! Et voi jakaa luvulla 0.")
    elif choice == 7:
        num1 = get_integer_input("Anna luku: ")
        num2 = get_integer_input("Anna luku: ")
    elif choice == 8:
        break
    else:
        print("Virheellinen valinta!")