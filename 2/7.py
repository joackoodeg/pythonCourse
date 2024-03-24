N = int(input("Introduce un número entero N: "))
# Inicializa un contador
# Usa un bucle para contar los dígitos de N
# Imprime el número de dígitos
i=0
while N != 0:
    N//=10 ## // es el operador de división entera 
    ## divide el valor actual de N por 10 y luego asigna el resultado de esa división de nuevo a N
    i+=1 

print("El número de dígitos es:", i)