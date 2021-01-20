miDiccionario = {"Alemania": "Berlin", "Francia": "Paris", "Reino Unido": "Londres", "España": "Madrid"}
miDiccionario["Italia"] = "Lisboa"
del miDiccionario["Reino Unido"]

print(miDiccionario["Francia"])
print(miDiccionario)

miTupla = ("Alemania", "Francia", "Reino Unido", "España")
miDiccionario = {miTupla[0]: "Berlin", miTupla[1]: "Paris", miTupla[2]: "Londres", miTupla[3]: "Madrid"}

print(miDiccionario)
print(miDiccionario.keys())
print(miDiccionario.values())
