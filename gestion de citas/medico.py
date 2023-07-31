from usuario import *
from Consulta import *
from especialidad import *

class medico (usuario):
    def __init__(self, Id, Nombre, Apellido, Telefono, Correo, Password,consultorio):
        
        self.__nombre = Nombre
        self.__Apellido = Apellido
        self.__Telefono = Telefono
        self.__Correo = Correo
        self.__password = None
        self.__consultorio=consultorio

 ##Añade Especialidad##
    def agregar_especialidad (self, Id , Nombre_Especilidad , Codigo_especialidad):
        self.__Id.append (Id)
        self.__Nombre_Especialidad.append (Nombre_Especilidad)
        self.__Codigo_especialidad.append (Codigo_especialidad)

def setConsultorio (self, Name):
            for i in self.__requerimientos_especiales:
                  if Name == i:
                        indice = self.__Consultorio.index(i)
                        self.__Consultorio.pop(indice)
                        self.__requerimientos_especiales.insert(indice)


#setters#
  
def setNombre (self, Nombre):
        self.__nombre = Nombre

def setApellido (self, Apellido):
       self.__apellido = Apellido

def setTelefono (self, Telefono):
        self.__telefono = Telefono
    
def setCorreo (self, Correo):
        self.__correo = Correo
    
def setPassword (self, Password):
        self.__password = Password

def setConsultorio (self, Consultorio):
        self.__Consultorio = Consultorio

    ### Getters ###

def getNombre (self):
        return self.__nombre
    

def getApellido (self):
        return self.__Apellido

def getTelefono (self):
        return self.__telefono

def getCorreo (self):
        return self.__correo


def getPassword (self):
        return self.__password

def getConsultorio(self):
        return self.__Consutorio
