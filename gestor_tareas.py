from bd_connect import *
from funciones import *
from agregar import opcion_1
from buscar import opcion_2
from editar import opcion_3
from completar import opcion_4
from pendientes import opcion_5
from completas import opcion_6
from todas import opcion_7
def main():
    while True:
        vencen=vencimientos()
        print(f"Cantidad de tareas vencidas: {vencen[0]}")
        print(f"Cantidad de tareas que vencen en un dia: {vencen[1]}")
        print("")
        accion=input(f"""Seleccione entre una de estas opciones:
                    1) agregar tarea
                    2) buscar tarea
                    3) editar tarea
                    4) completar una tarea
                    5) mostrar todas las tareas pendientes
                    6) mostrar todas las tareas completas
                    7) mostrar todas las tareas
                    0) salir         
: """)
        match accion:
            #flujo para agregar una tarea
            case "1":
                opcion_1()
            # flujo para buscar una tarea
            case "2":
                eleccion=input(f"""Elija una de las opciones a buscar:
                                1) titulo
                                2) fecha de vencimiento
                                3) prioridad
: """)
                match eleccion:
                    #buscar tarea por titulo
                    case "1":
                        titulo=input("Ingrese el titulo a buscar por titulo: ").lower()
                        try:
                            opcion_2(eleccion,titulo=titulo)
                        except:
                            print("-----------------------------------------")
                            print("|No se encontro una tarea con ese titulo|")
                            print("-----------------------------------------")
                    # buscar tarea por fecha de vencimiento
                    case "2":
                        print("Ingrese la tarea a buscar por fecha de vencimiento: ")
                        fec_venc=fecha_vencimiento(eleccion=eleccion) 
                        try:  
                            opcion_2(eleccion,fec_venc=fec_venc)                
                        except:
                            print("----------------------------------------")
                            print("|No se encontro una tarea con esa fecha|")
                            print("----------------------------------------")
                    # buscar tarea por prioridad
                    case "3":
                        priori=prioridad()
                        try:
                            opcion_2(eleccion,priori=priori)
                        except:
                            print("----------------------------------------")
                            print("|No se encontro una tarea con esa fecha|")
                            print("----------------------------------------")
            # flujo para editar una tarea     
            case "3":
                titulo=input("Ingrese titulo de la tarea: ")
                print("")
                comprobar=opcion_3(titulo)
                if comprobar==2:
                    print("---------------------")
                    print("|No existe la tarea.|")
                    print("---------------------")
                else:
                    opcion=input(f"""elija una de las opciones a editar:
                                    1) titulo
                                    2) descripcion
                                    3) fecha de vencimiento
                                    4) prioridad
    : """)
                    resultado=opcion_3(titulo,opcion=opcion)
                    if resultado == 1:
                        print("--------------------------------------------------")
                        print("|No se puede editar una tarea completa o vencida.|")
                        print("--------------------------------------------------") 
                    else:
                        print("-------------------------")
                        print("|Se ha editado la tarea.|")
                        print("-------------------------")
            #flujo para marcar una tarea como completa
            case "4":
                try:
                    titulo=input("Ingrese la tarea a completar: ")
                    opcion_4(titulo)
                except TypeError:
                    print("---------------------")
                    print("|La tarea no existe.|")
                    print("---------------------")
            # flujo para mostrar las tareas pendientes
            case "5":
                try:
                    opcion_5()
                except TypeError:
                    print("--------------------------")
                    print("|No hay tareas pendientes|")
                    print("--------------------------")
            #flujo para mostrar las tareas que ya estan completas
            case "6":
                try:
                    opcion_6()
                except TypeError:
                    print("-------------------------")
                    print("|No hay tareas completas|")
                    print("-------------------------")
            #flujo para mostrar todas las tareas
            case "7":
                try:
                    opcion_7()
                except TypeError:
                    print("-------------------")
                    print("|No existen tareas|")
                    print("-------------------")
            case "0":
                break
            case _:
                print("-------------------------")
                print("|elija una opcion valida|")
                print("-------------------------")
        input()
    conexion.close()
