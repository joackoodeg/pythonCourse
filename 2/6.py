N = int(input("Introduce un número N: "))
suma = 0
# Usa un bucle para sumar todos los números pares hasta N
# Imprime la suma de los números pares
i=0
suma=0
while(i!=N):
    if(i%2==0): suma+=i
    i+=1
     

print(suma)