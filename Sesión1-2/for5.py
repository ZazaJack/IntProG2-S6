def numeros_pares():
    numero = int(input("Ingrese un número positivo: "))
    for i in range(0, numero + 1):
        if i % 2 == 0:
            print(i)
102
def main():
    numeros_pares()

main()