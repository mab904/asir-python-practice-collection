class Modulo: #clase que representa un asignatura
    def __init__(self, nombre):
        self.nombre = nombre #nombre de la asignatura
        self.convocatoria = 4 #convocatorias disponibles
        self.nordinario = 0 #nota ordinaria obtenida
        self.nextraordinaria = 0 #nota extraordinaria obtenida

    def set_nota_ordinaria(self,nota):
        self.nordinario = nota #establece la nota ordinaria

class Alumno:
    def __init__(self, nombre, apellidos): #clase que representa a un alumno con sus modulos
        self.nombre = nombre
        self.apellidos = apellidos
        self.lista_modulos = []

    def Agregar_Modulo(self,modulo): #añade un modulo a un alumno en concreto
        self.lista_modulos.append(modulo)

    def set_nota_alumno(self,modulo,nota): #añade una nota a un modulo de un alumno en concreto
        for n in self.lista_modulos:
            if n.nombre == modulo:
                n.set_nota_ordinaria(nota)

    def nota_media_alumno(self): #media del alumno
        nota = 0
        for modulo in self.lista_modulos:
            nota += modulo.nordinario
        media = nota / len(self.lista_modulos)
        return media

class Clase: #clase que representa un conjunto de alumnos
    def __init__(self,nombre):
        self.nombre = nombre
        self.lista_alumnos = []
    def Agregar_Alumno(self,alumno): #agregar alumno a la clase "clase" xd
        self.lista_alumnos.append(alumno)

    def set_nota_modulo_alumno(self, n_alumno,n_modulo,nota): #funcion que busca a un alumno en concreto y le asigna una nota en una asignatura en concreto
        for alumno in self.lista_alumnos:
            if alumno.nombre == n_alumno:
                alumno.set_nota_alumno(n_modulo,nota)

#crear asignaturas
LM = Modulo("Lenguaje de Marcas")
FP = Modulo("Fundamentos de Programación")
PAR = Modulo("Redes")
 
 #crear alumnos y una clase
alumno1 = Alumno("Oscar", "Serano Balbao")
alumno2 = Alumno("Alexander", "Sarango Ecuador")
alumno3 = Alumno("Pedro", "Sanchez Junior")
asir1 = Clase("ASIR1")

#añadir alumnos
asir1.Agregar_Alumno(alumno1)
asir1.Agregar_Alumno(alumno2)
asir1.Agregar_Alumno(alumno3)

#matricular a los alumnos en modulos
alumno1.Agregar_Modulo(LM)
alumno1.Agregar_Modulo(FP)
alumno1.Agregar_Modulo(PAR)

alumno2.Agregar_Modulo(LM)
alumno2.Agregar_Modulo(FP)
alumno2.Agregar_Modulo(PAR)

alumno3.Agregar_Modulo(LM)
alumno3.Agregar_Modulo(FP)
alumno3.Agregar_Modulo(PAR)