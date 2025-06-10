
#Bienvenida

import random
Dado = random.randint(1, 6)
Gato= [n  for n in range (9)]
print(Gato)

tablero = [[(i*9) + h for h in range(10)] for i in range (9)]
for i in tablero:
    for h in i:
        print(h, end=" ")

    print()
