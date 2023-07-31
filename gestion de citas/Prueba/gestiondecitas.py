from sys import path
path.append("gestion de citas")

from Consulta import *
from medico import *
from especialidad import *
from paciente import *


###gestion de  citas###
obj1 = Consulta (10/3/21,3/5/22 , "gastitris" ,"")
obj2 = medico (2 , "Maria" ,"perez", 34312342 , "Maria123l@gmail.com" , "Maria" ,"otorrino")
obj3 = paciente (1 , "Pedro" , "Martinez" , 3203960622 , "pedrismar8@gmail.com" , "pedro")
obj4 = especialidad ("2","cirujano",43)

print("Ingresa al modulo:")
print("1.Consulta")
print("2.Paciente")
print("3.Medico")
print("4.Especialidad")
gestionar_citas = int(input("Digita el modulo a gestionar: "))
match gestionar_citas:
    case 1:
        print(" Realiza gestion de:")
        print("1. Consulta") 
        clases = 1
        while clases != 0 :
            clases = int(input("Digita la clase que quieres gestionar: "))
            match clases:
                case 1:
                    print("Que quieres hacer con esta clase?")
                    print("1. agendar cita no superior(1 MES)")
                    print("2. consultar citas agendadas")
                    print("3. Visualizar citas ")
                    print("4.enlistar citas")
                    print("5.eliminar citas")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            sete = int(input(" Desea realizar la agenda tu cita: "))
                            print(" 1.Si ")
                            print("2. No")
                        

                            print(obj1.getfecha_diponible)
                            print(obj1.getfecha_agendamiento)
                            print(obj1.get.motivo)
                            print(obj1.get.eliminar_cita)
                            print(obj1.getNombre)
                            print(obj1.getApellido)
                            print(obj1.getTelefono)
                            print(obj1.getCorreo)
                            print(obj1.getPassword)

                        case 2:
                            print(" Realiza la consulta de tus citas ")
                            print("1.Si  ")
                            print("2.No  ")
                            
                            sete = int(input("Dijita la consulta de tu cita: "))
                            match sete:
                                case 1:
                                    x = input("Selecciona la cita a consultar: ")
                                    obj1.setNombre(x)

                        case 3:
                            print(" Deseas Visualizar las citas ")
                            print("1.Si  ")
                            print("2.No  ")
                            
                            sete = int(input("Dijita la cita a visualizar: "))
                            match sete:
                                case 1:
                                    x = input("Selecciona Cita: ")
                                    obj1.setNombre(x)

                        case 4:
                            print(" Selecciona Las Citas a enlistar ")
                            print("1.Agendas  ")
                            print("2.No agendadas ")
                            
                            sete = int(input("Filtra la lista de citas: "))
                            match sete:
                                case 1:
                                    x = input("Selecciona lista de citas: ")
                                    obj1.setNombre(x)
    
                        case 5:
                            print(" Realiza la cancelacion con 2 horas de anticipacion ")
                            print("1.eliminar_cita  ")
                            
                            sete = int(input("Dijita la cancelacion de tu cita: "))
                            match sete:
                                case 1:
                                    x = input("Digita la cita a cancelar: ")
                                    obj1.setNombre(x)
                case 2:
                    print(" Verificar Consultorio")
                    print("2.Consultorio ")
                    opciones = int(input("Digita la opcion que quieres hacer: "))
                    match opciones:
                        case 1:
                            print(obj2.getNombre)
                            print(obj2.getApellido)
                            print(obj2.getTelefono)
                            print(obj2.getCorreo)
                            print(obj2.getPassword)
                            print(obj2.get.Consultorio)
                        case 2:
                            print("Verificar Consultorio")
                            print("1.Consultorio")
                           
                            sete = int(input(" Verificar Consultorio: "))
                            match sete:
                                case 1:
                                    x = input("Digita la Verificacion: ")
                                    obj2.setNombre(x)
                        
           
        pass