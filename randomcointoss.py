
import random

print("Heitätään kolikkoa viidesti:")

for i in range(5):
    result = random.randint(0,1)
    if result == 0:
	    print("Klaava!")
    else:
	    print("Kruuna!")