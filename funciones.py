# Clase de funciones

nombre = "Oscar"
num1=2
num2=3

def saludo():
    print(f"Hola mucho gusto {nombre}")

def sumar():
    num1 = 10
    num2 = 20
    #print(num1 + num2)
    suma = num1 + num2
    return suma

def resta(a,b):
    resta = a - b
    return resta

#saludo()
#print(sumar() + 10)

print(resta(num1,num2) + 10)