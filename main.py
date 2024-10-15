from suma import suma

def main():
    while True:
        print("Operaciones matematicas:")
        print("1. Suma de dos números")
        print("0. salir")
        
        opcion = input("elige una opcion: ")
        
        if opcion == '0':
            print("saliendo de la calculadora")
            break
        a = float(input("introduce el primer numero: "))
        b = float(input("introduce el segundo numero: "))
        
        if opcion == '1':
            print("resultado: ", suma(a, b))
            
if __name__== "__main__":
    main()