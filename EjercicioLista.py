#Crear lista con los nombres de su familia.

milistanombredefamilia=["Evanglina","Juan Cruz","Carolina","Ana María","Dora","Tomás"]

print("Mi familia está compuesta por:")
print(milistanombredefamilia)

# Ordenar alfabéticamente la lista de los nombres de familia.
milistanombredefamilia.sort()

print("Integrantes de mi familia ordenado alfabéticamente:")
print(milistanombredefamilia)

# Quitar de la lista de los nombres de familia, a tus abuelos.
milistanombredefamilia.remove("Ana María")
milistanombredefamilia.remove("Dora")

print("Mi familia sin abuelos:")
print(milistanombredefamilia)


# Crear lista con los valores de la temperatura de un mes entero (mes a elección, pero definirlo).

milistatemperaturasEnero2023=[20,21,20,24,25,27,26,25,25,28,25,30,31,29,28,28,29,30,31,33,32,29,27,26,26,25,27,29,30,30,33]

print("Las temperaturas del mes de Enero 2023 fueron:")
print(milistatemperaturasEnero2023)

# Ordenar ascendentemente la lista de temperaturas.
milistatemperaturasEnero2023.sort()
print("Las temperaturas de Enero en orden ascendente:")
print(milistatemperaturasEnero2023)

# Agregar en la lista de temperaturas, las temperaturas de los 15 días del mes siguiente.

milistatemperaturasFebrer2023=[28,28,30,33,32,29,27,26,26,25,27,29,30,30,33]

print("Los valores de temperatura de Enero y los 15 días del mes Febrero fueron:")
milistadetemperaturas=milistatemperaturasEnero2023+milistatemperaturasFebrer2023
print(milistadetemperaturas)


#Crear lista con los nombres de ciudades que hayan visitado.

milistaciudades=["Córdoba","Santa Fé","Bueno Aires","Bariloche","Salta","Tucumán","Jujuy","San Luis","Mendoza","Entre Río"]

print("Las ciudades visitadas fueron:")
print(milistaciudades)

# Quitar de la lista de ciudades la ciudad menos linda que hayas visitado.

milistaciudades.remove("Santa Fé")

print("Las ciudades visitadas mas lindas:")
print(milistaciudades)


#Crear lista con las fechas y nombres de eventos importantes de su vida.

milistafechasyeventos=["13 de enero: cumpleaños de hija","23 de junio: cumpleaños de Papá","7 de octubre: cumpleaños de Mamá","31 de octubre: cumpleaños de hijo"]

print("Las fechas importantes del año son:")
print(milistafechasyeventos)