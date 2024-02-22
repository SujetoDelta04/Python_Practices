def suma(num1, num2, name):
    
    result=(num1+num2)
    saludo="Hola " + name + " el resultado de los numeros que ingresaste es: " + str(result)

    return saludo;

print("Hola, digita tu nombre")
nombre=input()
print("Digita un numero")
n1=input()
print("Digita un segundo numero")
n2=input()

call=suma(int(n1), int(n2), nombre)

print(call)