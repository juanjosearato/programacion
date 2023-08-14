# Crear el siguiente diccionario:
# Las claves serán los dni de su núcleo familiar, y el valor será SOLO el nombre de la persona.

miDiccionario={52274555:"Juan Cruz", 50576208:"Evangelina",26945212:"Carolina",30196509:"Juan José"}

print(miDiccionario)

# Luego deberán añadir los datos de familia ampliada (abuelos, familia política, etc)

miDiccionario={10555608:"Dora",6708679:"Ana María"}

print(miDiccionario)


# Crear un nuevo diccionario con claves autogeneradas y valores de números de teléfono. Integré tupla en diccionario
# Ambos deben ser mostrados.

mitupla=("Teléfono 1","Teléfono 2","Teléfono 3")
miDiccionario1={mitupla[0]:351457895,\
                mitupla[1]:3576457890,\
                mitupla[2]:3576451039}

print(miDiccionario1)
print(miDiccionario1.keys())
print(miDiccionario1.values())
