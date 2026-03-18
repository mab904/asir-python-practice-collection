class Coche: #clase génerica 
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_año(self):
        print(f"{self.ano}")
    def __str__(self):
        return f"Coche {self.marca}, {self.modelo}, {self.ano}"


class CocheElectrico(Coche): #clase que hereda de coche
    def __init__(self, marca, modelo, ano, autonomia):
        super().__init__(marca, modelo, ano)
        self.autonomia = autonomia

    def mostrar_autonomia(self):
        print(f"{self.autonomia}")
    def __str__(self):
        return f"Coche {self.marca}, {self.modelo}, {self.ano}, {self.autonomia}"


class Concesionario: #clase que almacena otra clases (en este caso la clase coche y una clase heredada)
        def __init__(self):
            self.lista_coches = []

        def agregar_coche(self,coche):
            self.lista_coches.append(coche)

        def mostrar_coches(self):
            texto =""
            for coche in self.lista_coches:
                texto += coche.__str__() + " \n"

            return f" {texto}"
        def buscar_por_marca(self, busqueda): #funcion que busca por la marca
            lista = []
            for coche in self.lista_coches:
                if coche.marca == busqueda:
                    lista.append(coche)
            for i in lista:
                print(i)

#Ejemplos
coche1 = Coche("Ferra", "A", "2021")
coche2 = CocheElectrico("Tesla", "C", "2019", "3000 km")
coche3 = CocheElectrico("Tesla", "W", "2222", "4400 km")
#Crear un objeto de la clase concesionario y agregar objetos de la clases de coche
concesionario = Concesionario()
concesionario.agregar_coche(coche1)
concesionario.agregar_coche(coche2)
concesionario.agregar_coche(coche3)
#Probar las funciones
print(concesionario.mostrar_coches())
concesionario.buscar_por_marca("Tesla")