class Libro: #clase que representa un libro con su autor
    def __init__(self,titulo,autor): #constructor y atributos
        self.titulo = titulo 
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
class Biblioteca: #clase que almacena otra clase
    def __init__(self): 
        self.libros = [] #lista donde se guardan objetos de la clase libro
    def agregar_libro(self,libro): #funcion para agregar un libro a la lista
        self.libros.append(libro)
    def mostrar_libros(self):
        if self.libros == []:
            return "Biblioteca Vacia Melon" #en caso de que la lista este vacía
        else:
            cadena= ""
            for libro in self.libros:
                cadena += libro.__str__() + "\n"
            return cadena

#crear libros
libro1 = Libro("La vida es sueño", "Calderón de la Barca")
libro2 = Libro("Sidi", "Pérez Reverte")
#crear biblioteca
biblioteca = Biblioteca()
#añadir libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

print(biblioteca.mostrar_libros())