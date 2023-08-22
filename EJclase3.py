"""""
Se solicita construir un sistema que permita almacenar datos de pacientes, médicos y enfermeras.
Los  pacientes  tienen  información  de  nombre,  cédula,  género  y  servicio,  que  corresponde 
al  servicio donde están alojados.Las enfermeras tienen la misma información que los pacientes, 
menos servicio, mas turno (que puedeser 7-19, 19-7, corrido) y rango (auxiliar, jefe, jefe del servicio ).
Adicionalmente  pueden  existir  médicos  que  tienen  toda  la  información  de  las  enfermeras,  
menos  el rango, más especialidad
"""""

#Base de la herencia
class Persona():
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0
        self.__genero = ""
    
    def asignarNom (self, nombre):
        self.__nombre = nombre
    
    def asignarCedula (self, cedula):
        self.__cedula = cedula

    def asignarGen (self, genero):
        self.__genero = genero

    def verNom (self):
        return  self.__nombre 
    
    def verCedula (self):
        return  self.__cedula 
    
    def verGen (self):
        return  self.__genero
    
class Paciente(Persona):
    def __init__(self):
        Persona.__init__(self)
        self.__servicio = ""

    def asignarServicio (self, servicio):
        self.__servicio = servicio

    def verServicio (self):
        return  self.__servicio
        
class Empleado_Hosp(Persona):
        def __init__(self):
            self.__turno = ""

        def asignarTurno(self, turno):
            self.__turno = turno

        def verTurno (self):
            return  self.__turno
        

class Enfermera(Empleado_Hosp):
    def __init__(self):
        self.__rango = ""
    
    def asignarRango(self, rango):
            self.__rango = rango

    def verRango(self):
            return  self.__rango
        
        
class Medico(Empleado_Hosp):
    def __init__(self):
        super().__init__(self)
        self.__especialidad = ""

    def asignarEspecialidad(self, especialidad):
            self.__especialidad = especialidad

    def verEspecialidad(self,):
            return  self.__especialidad
        
BD = {}    

while True:
     print("Bienvenido al sistema informativo del hospitalX, a continuación podrá ver las opciones disponibles\n del programa")
     men1 = input(int(( "1. Ingresar información\n 2.Ver información\n3.Salir")))
     if men1 == 1:
        
        op1 = input(int("Usted está a punto de ASIGNAR información acerca de alguno de los siguientes 3 perfiles:\n 1.Paciente \2.Enfermera(o)\n3.Médico\n 4.salir al menú principal"))
        while op1 != 4 and range (0,5):
            if op1==1 :
               p = Paciente()
               p.asignarNom(input ("Ingrese el nombre del paciente a registrar"))
               p.asignarCedula(input ("Ingrese la cédula del paciente a registrar"))
               p.asignarGen(input ("Ingrese el género del paciente a registrar,\n para mayor facilidad use únicamente M para maculino, F para femenino"))
               BD[p.verCedula] = p
            if op1 == 2:
             e = Enfermera()
             e.asignarNom(input("Ingrese el nombre del personal de enfermería a registrar"))
             e.asignarCedula(input("Ingrese la cédula del personal de enfermería a registrar"))
             e.asignarGen(input("Ingrese el género del personal de enfermería a registrar,\n para mayor facilidad use únicamente M para maculino, F para femenino"))
             e.asignarTurno(input("Ingrese el turno del personal de enfermería a registrar,\n recuerde que las opciones son 1.7-19\n 2.19-7\n 3.corrido"))
             e.asignarRango(input("Ingrese el rango del personal de enfermería a registrar"))
             BD[e.verCedula] = e
            if op1 == 3:
             m = Medico()
             m.asignarNom(input("Ingrese el nombre del personal mèdico registrar"))
             m.asignarCedula(input("Ingrese la cédula del personal mèdico  a registrar"))
             m.asignarGen(input("Ingrese el género del personal mèdico a registrar,\npara mayor facilidad use únicamente M para maculino, F para femenino"))
             m.asignarTurno(input("Ingrese el turno del personal mèdico a registrar,\nrecuerde que las opciones son 1.7-19\n 2.19-7\n 3.corrido"))
             m.asignarRango(input("Ingrese el rango del personal mèdico a registrar"))
             BD[m.verCedula] = m
        
        if men1 ==2:    
            men2= input(int("Usted está a punto de VER información acerca de alguno de los siguientes 3 perfiles:\n 1.Paciente \2.Enfermera(o)\n3.Médico\n 4.salir al menú principal"))
            while op1 != 4 and range (0,5):
                if men2 == 1:
                    cc = input(int("Ingrese la cèdula del paciente del cual desea la informaciòn,\nevite incluir puntos (.) o espacios de por medio"))
                    if cc == p.verCedula():
                        print(BD.get(cc,"No esta en la Base de Datos").verNombre()) ;"""""no entiendo muy bien ESTA lìnea"""""
                    else: 
                        print("La información correspondinte a la cédula que busca no se encuentra en la sección de los pacientes")
              
                if men2 == 2:
                      cc = input(int("Ingrese la cèdula del paciente del cual desea la informaciòn,\nevite incluir puntos (.) o espacios de por medio"))
                      if cc == e.verCedula():
                            print(BD.get(cc,"No esta en la Base de Datos").verNombre()) 
                      else: 
                           print("La información correspondinte a la cédula que busca no se encuentra en la sección del personal de enfermería")

                if men2 ==3:
                      cc = input(int("Ingrese la cèdula del paciente del cual desea la informaciòn,\nevite incluir puntos (.) o espacios de por medio"))
                      if cc == m.verCedula():
                        print(BD.get(cc,"No esta en la Base de Datos").verNombre())
                      else: 
                           print("La información correspondinte a la cédula que busca no se encuentra en la sección del personal médico")
        
        if men1 ==3:
            break


