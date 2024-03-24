from math import sqrt

numero = float(input("Introduce un número (negativo para terminar): "))

# En un bucle, verifica si el número es negativo; si lo es, termina el bucle
# Calcula la raíz cuadrada del número

# Imprime la raíz cuadrada
while(numero>0):
    raiz= sqrt(numero)
    print(raiz)
    numero = float(input("Introduce un número (negativo para terminar): "))
