def tabla_multiplicar(num): 
        for i in range(1, 11):
            print(f"{num} x {i} = {num * i}")
            
def main():
    num = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
    tabla_multiplicar(num)


main()