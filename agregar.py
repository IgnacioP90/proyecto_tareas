from bd_connect import *
from funciones import *
def opcion_1():
    titulo=input("Ingrese titulo de la tarea: ")
    desc=input("Ingrese una breve descripcion: ")
    print("ahora debera ingresar una fecha de vencimiento:")
    fec_venc=fecha_vencimiento() # Funcion fecha de vencimiento donde ingreso la fecha y la valido
    priori=prioridad() # Cree una funcion prioridad para que solo haya 3, alta media o baja
    titulo=titulo.lower()
    try:
        agregar_tarea(titulo,desc,fec_venc,priori)
        print("-------------------------")
        print("Tarea agregada con exito!")
        print("-------------------------")
    except sqlite3.OperationalError:
        print("-------------------------------------")
        print("no se ha podido realizar la operacion")
        print("-------------------------------------")
    except sqlite3.IntegrityError:
        print("--------------------")
        print("Ya existe esa tarea.")
        print("--------------------")