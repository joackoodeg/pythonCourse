N = int(input("Introduce un número entero N para convertirlo a binario: "))

binario = []

# Divide sucesivamente por 2 y guarda los restos
while N > 0:
    r = N % 2
    binario.insert(0, r)  # Inserta el resto al principio de la lista
    N //= 2

print("El número", N, "en binario es:", binario)