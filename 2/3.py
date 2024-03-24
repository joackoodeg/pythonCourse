N = int(input("¿Cuántos números deseas promediar? "))
suma = 0
# Usa un bucle para solicitar N números, sumarlos y luego calcular la media
# Imprime la media
i=0
while(i!=N):
    x=int(input("inserte nro: "))
    suma+=x
    i+=1

# Imprime la suma total
print("El promedio es: ", suma/N)