
def mostrarNumeros(inicio=0, fin=0):
    if(inicio < fin): 
        for i in range(inicio, fin+1):
            print(i, end=" ")
    else:
        for i in range(inicio, fin-1, -1):
            print(i, end=" ")
            
            
def main():
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número de fin: "))
    mostrarNumeros(inicio, fin)
    
main()
