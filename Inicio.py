
#Bienvenida

import random
Dado = random.randint(1, 6)
Lados= [n  for n in range (9)]
for l in (Lados):
  l=["▭","▭","▭","▭","▭","▭","▭","▭","▭"]
  for i in l:
    i=("▭")
    print(i, end="  ")
  print()
