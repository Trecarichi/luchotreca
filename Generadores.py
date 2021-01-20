from _ast import For
from typing import Tuple


# def generaPares(lim):

#   num = 1
#    miLista=[]
#
#   while num < lim:
#       miLista.append(num*2)
#       num = num+1
#   return miLista


# print(generaPares(10))

def generaPares(lim):
    num = 1

    while num < lim:
        yield num * 2
        num = num + 1


devuelvePares = generaPares(10)

# for i in devuelvePares:
#    print(i)


print(next(devuelvePares))
print("aqui va mas codigo...")
print(next(devuelvePares))


def devuelveCiudades(*ciudades):
    for elemento in ciudades:
        #for subElemento in elemento:
            yield from elemento


ciudades_devueltas = devuelveCiudades("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudades_devueltas))
print(next(ciudades_devueltas))
