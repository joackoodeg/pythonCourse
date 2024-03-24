N = int(input("¿Cuántos números vas a introducir? "))
# Inicializa una variable para guardar el máximo valor
# Usa un bucle para solicitar N números y encontrar el máximo
# Imprime el número máximo
max = -1
i=0
while(i!=N):
    x=int(input("inserte nro: "))
    if(x>max): max=x
    i+=1

print("el max es: ", max)