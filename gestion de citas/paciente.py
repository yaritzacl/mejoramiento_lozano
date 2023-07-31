from usuario import *
from Consulta import *

class paciente (usuario):
      def __init__(self, Id, Nombre, Apellido, Telefono, Correo, Password, ):
      
        self.__nombre = Nombre
        self.__Apellido = Apellido
        self.__Telefono = Telefono
        self.__Correo = Correo
        self.__password = None

 ##setters##
    
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

def setCosultar_citas (self, Cosultar_citas):
        self.__Cosultar_citas = Cosultar_citas


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


