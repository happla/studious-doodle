
### put your code here ###
def bubble_sort(number):
    for i in range(len(number)):
        for j in range(len(number)-i-1):
            if number[j] > number[j+1]:
                number[j], number[j+1] = number[j+1], number[j]
    return number
a = []
number = int(input("Anna lajiteltavien numeroiden lukumäära: "))
for i in range(number):
    value = int(input("Anna taulokukon %d numero: "%i))
    a.append(value)
print("Lajiteltu lista nousevassa järjestyksessä.", bubble_sort(a))