from paciente import *
from medico import*
from paciente import paciente
class Consulta:
      def __init__(self,fecha__agendamiento, fecha__disponible,motivo__cita,eliminar__cita):
       self.__fecha__agendamiento=fecha__agendamiento
       self.__fecha__disponible=fecha__disponible
       self.__motivo__cita=motivo__cita
       self.__eliminar__cita=eliminar__cita
       
    
    #agenda cita#  
      def agendar_cita_paciente (fecha__agendamiento, fecha__disponible,motivo__cita,eliminar__cita,self, Id, Nombre, Apellido, Telefono, Correo, Password):
            print ("QUIERES REALIZAR EL AGENDAMIENTO DE LA CITA NO SUPERIOR A UN MES")
            print ("1.Si")
            print ("2.No")
            selector = int(input())
            match selector:
                  case 1:
                        self.__agendar = "Agendamiento de citas"
                        obj1 = paciente (Id , Nombre , Apellido , Telefono , Correo , Password)
                        obj2 = Consulta (fecha__agendamiento, fecha__disponible,motivo__cita,eliminar__cita)
                        self.__id.append(Id)
                        self.__nombre.append(Nombre)
                        self.__apellido.append(Apellido)
                        self.__telefono.append(Telefono)
                        self.__correo.append(Correo)  
                        self.__password = Password
                        self.__fecha__agendamiento=fecha__agendamiento
                        self.__fecha__disponible=fecha__disponible
                        self.__motivo__cita=motivo__cita
                        self.__eliminar__cita=eliminar__cita
                        return self.__agendar
                  case 2:
                        print("No agendaste la cita")
            
 
     #Enlista Consulta Citas 
      def enlistar_consulta (self):
            for name in self.__fecha__agendamiento:
                  print(name)
            for motivo_cita in self.__motivo__cita:
                  print(motivo_cita)
  

   ##Añade paciente para las citas##
      def agregar_paciente (self, Id , Nombre , Apellido , Telefono , Correo , Password,):
        self.__Id.append (Id)
        self.__Nombre_Paciente.append (Nombre)
        self.__Apellido.append (Apellido)
        self.__Telefono.append (Telefono)
        self.__Correo.append (Correo)
        self.__Password.append (Password)
        

    ### Añadir Medico para la consulta por medio del paciente###

      def agregar_medico (self,Id , Nombre , Apellido , Telefono , Correo ,Password,Consultorio ):
        self.__Id.append (Id)
        self.__Nombre_Paciente.append (Nombre)
        self.__Apellido.append (Apellido)
        self.__Telefono.append (Telefono)
        self.__Correo.append (Correo)
        self.__Password.append (Password)
        self.__Consultorio.append (Consultorio)

#setters#
def setfecha_agendamiento (self,fecha_agendamiento):
       self.__fecha_agendamiento = fecha_agendamiento


def setfecha__disponible (self,fecha__disponible):
       self.fecha__disponible = fecha__disponible

def setmotivo (self,motivo):
       self.motivo = motivo

def setNombre (self, Nombre):
        self.__nombre = Nombre
    
def setTelefono (self, Telefono):
        self.__telefono = Telefono
    
def setCorreo (self, Correo:str):
        self.__correo = Correo
    
def setPassword (self, Password):
        self.__password = Password

    ### Getters ###
def getfecha_agendamiento(self):
       return self.__fecha_agendamiento

def getfecha_agendamiento(self):
       return self.__fecha_agendamiento

def getmotivo (self):
        return self.__motivo


def getId (self):
        return self.__id
    
def getNombre (self):
        return self.__nombre

def getApellido (self):
      return self.apellido

def getTelefono (self):
        return self.__telefono
    

def getCorreo (self):
        return self.__correo
    
    
def getPassword (self):
        return self.__password