import math
#Libreria que permite usar funciones como marh.trunc que sirve para tomar 
#la parte entera de un número
import os
#Perimite utilizar la funcion system(), que a su ves pausa el systema
# y no permite continuar hasta que el usuaria precione alguna tecla.

while True: #Aqui se va a crea un menú de 3 opciones.
    print("--------Sistema de rastreo de contactos simplificado para COVID-19--------")
    print("1. Cliente")
    print("2. Adminitrador")
    print("3. Salir")
    opc=int(input("Opción --> "))
    if (opc == 1):

        class cliente():
            #Se crea la clase cliente tal como se propone en el laboratorio.
            #Se definen también los atributos de la clase.

            def __init__(self,nombre,apellido,numero,estado,numVacuna):
                #__init__: es un constructor que nos ayudara a instanciar cada objeto que se valla a crear.
                self.nombre=nombre
                self.apellido=apellido
                self.numero=numero
                self.estado=estado
                self.numVacuna=numVacuna

            #A continuación se declaran los métodos.
            def usuario (self):
                #Con esta función se tomará el atributo (numero) como cadena de caracteres
                #Y se usarán los dos últimos espacios de dicha cadena 
                user= self.numero [8:]
                return (user)

            def contra (self):
                #En esta función se va a tomár el apellido y se lo va a poner en minúscula
                #y también se lo va a revertir, para poder crear una contraseña. 
                password="".join(reversed(self.apellido))
                contrasena=password.lower()
                return (contrasena)
            
        print("--------------------------------RESGISTRO--------------------------------")
        print("Para el resgistro de un nuevo cliente llene los siguientes campos")
        nombre=input("Digite su nombre: ")
        apellido=input("Digite su apellido: ")
        numero=input("Digite su número de teléfono: ")
        estado=input("¿Estado de salud?: normal - cercano - caso --> ")
        numVacuna=int(input("¿Cuántas dosis se ha colocado? "))
        while (numVacuna>4) or (numVacuna<0):
            print("No puede tener más de 3 vacunas")
            numVacuna=int(input("¿Cuántas dócis se ha colocado? "))

        #Se instancia el objeto cliente1 del tipo (cliente)
        cliente1=cliente(nombre,apellido,numero,estado,numVacuna)

        #Se concatena el nombre convertido a minúscula con los dos últimos espacios
        #del atributo (numero), para crear el usuario del cliente.
        user=cliente1.nombre.lower()+cliente1.usuario()

        #Aqui simplemente se imprime la función que contiene el apellido invertido en minúscula.
        print("***Su usuario es: --> "+user) #Imprimir usuario.
        password=cliente1.contra()
        print("***Su contraseña es: --> "+password)
        os.system("pause") #Función que pausa el sistema hasta que el usuario preciones una tecla.

        print("-----------------------------INICIAR SECIÓN--------------------------------")
        #Estructura de control para validar el usuario que se ingrese posteriormente a su registro
        while True:
            usuario=input("***Usuario: --> ")
            if (user!=usuario):
                print("X Usuario incorrecto, vuelva a intentarlo X")
            else:
                break
        #Estuctura de control para validar contraseña
        while True:
            contrasena=input("***Contraseña: --> ")
            if (password!=contrasena):
                print("X Contraseña incorrecto, vuelva a intentarlo X")
            else:
                break
        print("***INICIO DE SECIÓN EXITOSO***")
        os.system("pause")
        #Métodos que puede realizar el cliente...
        print("-----------------------------ACCIONES DE CLIENTES--------------------------------")
        while True:
            print("1. Registrarse en una tienda")
            print("2. Ver tiendas visitadas")
            print("3. Ver estado")
            print("4. Regresar")
            op=int(input("Opción --> "))
            if (op==1):
                print("-----------------------------RESGISTRO DE TIENDA--------------------------------")
                class tienda(cliente):
                    #Se crea una segunda clase
                    #Los atributos que poseen son los siguientes
                    def __init__(self,nombre,telefono,estado,gerente,horaRegistro):
                        self.nombre=nombre
                        self.telefono=telefono
                        self.estado=estado
                        self.gerente=gerente
                        self.horaRegistro=horaRegistro
                    #Métodos de la clase tipo tienda
                    def juzgar (self):
                        #Una condición para comprobar através del número de vacunas
                        # si un cliente es caso, cercano o normal. 
                        if ((cliente1.numVacuna)==0) or ((cliente1.numVacuna)==1):
                            print("Entonces tienes un estado de: caso")
                        else:
                            if ((cliente1.numVacuna)==2):
                                print("Entonces tienes un estado de: cercano")
                            else:
                                if ((cliente1.numVacuna)==3):
                                    print("Entonces tienes un estado de: normal")

                    def determinarEstado (self):
                        #Condición para determinar si hay contagio por los clientes 
                        #que se registran en la hora determinada.
                        if (self.horaRegistro=="12"):
                            print("estado: caso")
                        else:
                            if (self.horaRegistro=="11") or (self.horaRegistro=="13"):
                                print("estado: cercano")
                            else:
                                print("estado: normal") 
                #Datos para el regitro de objeto tienda1.
                print("Para registrar un tienda debe llenar los datos de la tienda")
                nombre=input("Nombre de la tienda: ")
                telefono=input("Teléfono de la tienda: ")
                estado=input("Estado de la tienda: ")
                gerente=input("Nombre de gerente de la tienda: ")
                hora=input("Hora en que registra la tienda (Formato: 00:00): ")
                horaRegistro=hora [:-3] #Comando para tomar la parte horaria de la hora ingresada. 
                tienda1=tienda(nombre,telefono,estado,gerente,horaRegistro)
                print("***Tienda reistrada con exito***")
                os.system("pause") #Pasusar el sistema.
            elif (op==2):
                #Imprimir datos de tienda registrada y visitada al mismo tiempo.
                print("-----------------------------TIENDAS VISITADAS--------------------------------")
                print("Usted visitó las siguietes tiendas:")
                print("")
                print("    1)     nombre: ",tienda1.nombre,"     tlf: ",tienda1.telefono,"     estado: ",tienda1.estado,"     gerente: ",tienda1.gerente)
                print("")
                os.system("pause") #Pasusar el sistema.
            elif (op==3 ):
                #Imprimir datos de cliente para determinar su estado.
                print("-----------------------------ESTADO--------------------------------")
                print("Su estado actua es el siguiente:")
                print("")
                print("nombre: ",cliente1.nombre,"          tlf: ",cliente1.numero,"          estado: ",cliente1.estado)
                print("")
                print("Su estado según el registro es el siguiente:")
                print("")
                print("nombre: ",cliente1.nombre)
                print("tlf: ",cliente1.numero)
                # Método que permite determinar si un cliente1 es caso, cercano o normal
                #atraves del horario de registro de tienda.
                tienda1.determinarEstado()
                os.system("pause") #Pasusar el sistema.
            elif (op==4):
                os.system("pause")
            else:
                print("Opción inválida, vuelva a intentarlo")
            if (op==4):
                break
    elif (opc == 2):
        #Adminitrador peude ver el toda la información sobre los cliente y tiendas registradas
        print("-----------------------Historial de visitas:-----------------------")
        print("")
        print("    1)     nombre: ",tienda1.nombre,"     tlf: ",tienda1.telefono,"     estado: ",tienda1.estado,"     gerente: ",tienda1.gerente)
        print("")
        print("Detalle de los clientes:")
        print("")
        print("nombre: ",cliente1.nombre)
        print("tlf: ",cliente1.numero)          
        tienda1.determinarEstado()
        os.system("pause") #Pasusar el sistema.
        print("-----------------------Desición de admin-----------------------")
        print("El señor/ar ",cliente1.nombre,", posse ",cliente1.numVacuna," dósis")
        tienda1.juzgar() #Método que permite decidir si un cliente es caso, cercano o normal atraveés de las dosis que contenga
        os.system("pause") #Pasusar el sistema.
    elif (opc == 3):
        print("MUCHAS GRACIAS")
        os.system("pause")
    else:
        print("Opción incorrecta, vuelva a intntarlo")
    if (opc == 3):
        break