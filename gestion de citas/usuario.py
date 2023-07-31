class usuario:
    def __init__ (self, id, nombre,apellido,telefono , correo,password):
       self.__id = id
       self.__nombre = nombre
       self.__apellido = apellido
       self.__telefono = telefono
       self.__correo = correo
       self.__password = password

### Setters ###

    def setNombre (self, Nombre):
        self.__nombre = Nombre
    
    def setTelefono (self, Telefono):
        self.__telefono = Telefono
    
    def setCorreo (self, Correo):
        self.__correo = Correo
    
    def setPassword (self, Password):
        self.__password = Password

    ### Getters ###


    def getId (self):
        return self.__id
    

    def getNombre (self):
        return self.__nombre
    

    def getTelefono (self):
        return self.__telefono

    def getCorreo (self):
        return self.__correo
    

    def getPassword (self):
        return self.__password
