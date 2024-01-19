# Author: Edwin Yovani Rodriguez Rivera
# IDGS802 - 21000445
import os

class OperaBas:
    cantidad=0

    def operacion(self):
        self.cantidad = int(input("¿Cuantos numeros va ingresar?"))
        numeros = []
        for i in range(self.cantidad):
            num = int(input("Ingrese el número: "))
            numeros.append(num)
    
        numeros = list(set(numeros))
        numeros.sort()
    
        for num in numeros:
            print(num)

        pares = [num for num in numeros if num % 2 == 0]
        pares.sort()
        print("Sus numeros en pares",pares)

        impares = [num for num in numeros if num % 2!= 0]
        impares.sort()
        print("Sus numeros en inpares",impares)

class piramides:
    cantidad_caracteres=0
    def construccion(self):
        self.cantidad_caracteres = int(input("Ingresa un numero para la construccion de la piramide :"))
        for i in range(1, self.cantidad_caracteres + 1):
            for j in range(i):
                print("*", end="")
            for j in range(self.cantidad_caracteres - i):
                print(" ", end="")
            print()



    


def main():
    #Lina para limpiar la terminal
    os.system('cls')
    obj = OperaBas()
    obj.operacion()
    obj2 = piramides()
    obj2.construccion()

if __name__ == "__main__":
    main()