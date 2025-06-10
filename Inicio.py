
#Bienvenida


import random
Dado1 = random.randint(1, 6)
Dado2=random.randint(1, 6)
print("El resultado es {} y {}".format(Dado1,Dado2))
Mueve1= (Dado1 + Dado2)
comomoverse=int(input("¿Desea mover únicamente una ficha o dos? Una: 1, Dos: 2 "))

if comomoverse==1:
  Ficha=int(input("¿Que ficha desea mover? (Indique el número de ficha) "))
  if Ficha == 1:
    print("F1 se ha movido {} espacios".format(Mueve1))
  elif Ficha == 2:
      print("F2 se ha movido {} espacios".format(Mueve1))
  elif Ficha == 3:
        print("F3 se ha movido {} espacios".format(Mueve1))
  elif Ficha == 4:
          print("F4 se ha movido {} espacios".format(Mueve1))
  elif Ficha == 2:
   print("F1 se ha movido {} espacios".format(Mueve1))

elif comomoverse==2:
  F1=int(input("¿Que ficha desea mover? "))
  F2=int(input("¿Que ficha desea mover? "))

Lados= [n  for n in range (9)]
for l in (Lados):
  l=["▭"]*9
  for i in l:
    i=["▭"]
    for h in i:
      print(h, end="  ")
  print()

