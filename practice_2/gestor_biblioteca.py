list_of_books={
            "La antologia del terror de HP Lovecraft":{
                  "Autor": "HP Lovecraft",
                  "Genero": "Terror",
                  "Año de publicacion": "1990"
            }
      }

option=6

def add_book():

        system_finale=1

        while system_finale != 0:

            print("Ingrese la informacion solicitada")
            print("Titulo del libro")
            title=input()
            print("Autor del libro")
            autor=input()
            print("Genero del libro")
            gender=input()
            print("Año de publicacion")
            year=input()

            if title == "" or autor == "" or gender == "" or year == "":
              print("Debes llenar toda la informacion solicitada para almacenar este libro")
            else:
                 new_book={
                    title:{
                        "Autor": autor,
                        "Genero":gender,
                        "AÑo de publicacion":year
                    }
                }
                 list_of_books[title]=new_book

                 print("Se añadio un nuevo libro al catalogo. ¿Deseas continuar? 1 = Si, 0 = No")
                 system_finale=int(input())
        

def view_all_books():
      print("*")
      print("")
      print("Libros disponibles")
      for fila in list_of_books:
            print("* " + fila)
      print("")
      print("*")

def search_books():
    
    print("Digita el titulo, genero o el autor del libro que deseas y buscaremos si esta")
    book=input()

    
 

while option != 0:

    print("Lista de opciones de libreria virtual")
    print("1. Agregar un libro")
    print("2. Ver libros disponibles")
    print("3. Buscar libros")
    print("4. Pedir un libro prestado")
    print("5. Devolver un libro")
    print("0. Salir del sistema")
    option=int(input())

    if option == 1:
        add_book()
    elif option == 2:
        view_all_books()
    elif option == 3:
         search_books()
