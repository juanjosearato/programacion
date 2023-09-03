
suma =0 
num= 0
while num!=-1:
    num=int(input("ingrese un numero positivo o negativo : "))
    if num !=-1:
        suma= suma +num
        print ("la sumatoria total de los numeros es" ,suma)

numeros= int (input("Cantidad de numeros a ingresar:  "))
nums=[]

for i in range(numeros):
    num= float (input(f"ingrese un numero <,>, o = a 0{i+1}: "))
    nums.append(num)
    Nmayor=0
    Nigual=0
    Nmenor=0
    for num in nums:
        if num >0 :
            Nmayor = Nmayor + 1
        elif  nums < 0 :
            Nmenor = Nmenor + 1

        else :
            Nigual = Nigual + 1

print (f"De los {numeros} numeros ingresados: ")
print (f"{Nmayor} son mayores que 0")
print (f"{Nigual} son iguales que 0.")
print (f"{Nmenor} son menores que 0 ")

vocales=["a","e","i","o", "u"]
caracter=input ("introduce un caracter : ")
while caracter !=0:
    if caracter in vocales:
        print ("VOCAL")
    else:
        caracter != vocales
        print ("NO VOCAL")
    caracter=input("ingrese otro caracter: ")
    if caracter ==0:
        print ("FIN DEL PROGRAMA")