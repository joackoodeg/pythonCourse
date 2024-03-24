N = int(input("¿Cuántos números deseas sumar? "))
suma = 0
# Usa un bucle para solicitar N números y sumarlos
i=0
while(i!=N):
    x=int(input("inserte nro: "))
    suma+=x
    i+=1

# Imprime la suma total
print(suma)