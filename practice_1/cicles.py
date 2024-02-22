def array_add(element):

    list_of_names=[]

    list_of_names.append(element)

    return list_of_names

def for_cicle(rango):
 
    for fila in range(rango):
        print(fila)

def while_cicle():

    contador=0

    while contador > 10:
        contador+=1
        print(contador)

menu=1

while menu != 0:

    print("Ciclos, Condicionales y Array")
    print("1. Array")
    print("2. For")
    print("3. While")
    print("4. Ver lista")
    option=int(input())

    if option == 1:
        op=1
        while op != 0:

            print("Digita un nombre")
            name=input()

            array_add(name)

            print("Si terminaste de añadir oprime 0 para salir")
            op=int(input())


    elif option == 2:

        print("Digita el rango que quieres que tenga el ciclo for")
        ran=int(input())
        print (for_cicle(ran))

    elif option == 3:

        print(while_cicle())

    elif option == 4:

        list_names=array_add("Fulano")

        for fila in range (len(list_names)):
            print(list_names[fila])

    print("Deseas terminar la ejecucion del programa? 1 = No, 0 = Si")
    menu=int(input())