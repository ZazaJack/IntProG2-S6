
def mostrarLetra(numero):
    for i in range(numero):
        print(f"a"*i)
        
def main():
    numero = int(input("Ingrese un número: "))
    mostrarLetra(numero)
    
main()