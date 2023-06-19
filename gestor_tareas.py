from src.bd_connect import *
from src.func.funciones import *
from src.options.agregar import opcion_1
from src.options.buscar import opcion_2
from src.options.editar import opcion_3
from src.options.completar import opcion_4
from src.options.pendientes import opcion_5
from src.options.completas import opcion_6
from src.options.todas import opcion_7
from src.options.eliminar import opcion_8
def main():
    while True:
        vencen=vencimientos()
        if vencen:
            if(vencen[0]>=1):
                print(f"Tienes {vencen[0]} tareas vencidas, tienes la posibilidad de editarlas si asi lo deseas.")
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
                    8) eliminar tarea
                    0) salir         
: """)
        match accion:
            #flujo para agregar una tarea
            case "1":
                opcion_1()
            # flujo para buscar una tarea
            case "2":
                result=opcion_7()
                if result:
                    eleccion=input(f"""Elija una de las opciones a buscar:
                                    1) titulo
                                    2) fecha de vencimiento
                                    3) prioridad
    : """)
                    match eleccion:
                        #buscar tarea por titulo
                        case "1":
                            titulo=title()
                            try:
                                opcion_2(eleccion,titulo=titulo)
                            except ValueError:
                                print("-----------------------------------------")
                                print("|No se encontro una tarea con ese titulo|")
                                print("-----------------------------------------")
                        # buscar tarea por fecha de vencimiento
                        case "2":
                            print("Ingrese la tarea a buscar por fecha de vencimiento: ")
                            fec_venc=fecha_vencimiento(eleccion=eleccion) 
                            try:  
                                opcion_2(eleccion,fec_venc=fec_venc)                
                            except ValueError:
                                print("----------------------------------------")
                                print("|No se encontroaron tareas con esa fecha|")
                                print("----------------------------------------")
                        # buscar tarea por prioridad
                        case "3":
                            priori=prioridad()
                            try:
                                opcion_2(eleccion,priori=priori)
                            except ValueError:
                                print("--------------------------------------------")
                                print("|No se encontraron tareas con esa prioridad|")
                                print("--------------------------------------------")
            # flujo para editar una tarea     
            case "3":
                titulo=title()
                print("")
                try:
                    opcion_2("1",titulo=titulo)
                    opcion=input(f"""elija una de las opciones a editar:
                                    1) titulo
                                    2) descripcion
                                    3) fecha de vencimiento
                                    4) prioridad
: """)
                    resultado=opcion_3(titulo,opcion)
                    if resultado == 1:
                        print("--------------------------------------------------")
                        print("|No se puede editar una tarea completa o vencida.|")
                        print("--------------------------------------------------") 
                    else:
                        print("-------------------------")
                        print("|Se ha editado la tarea.|")
                        print("-------------------------")
                except ValueError:
                    print("---------------------")
                    print("|No existe la tarea.|")
                    print("---------------------")      
            #flujo para marcar una tarea como completa
            case "4":
                try:
                    opcion_5()
                    print("")
                    print("Tarea a completar.")
                    titulo=title()
                    opcion_4(titulo)
                except ValueError:
                    print("-------------------------------")
                    print("|No hay tareas para completar.|")
                    print("-------------------------------")
            # flujo para mostrar las tareas pendientes
            case "5":
                try:
                    opcion_5()
                except ValueError:
                    print("--------------------------")
                    print("|No hay tareas pendientes|")
                    print("--------------------------")
            #flujo para mostrar las tareas que ya estan completas
            case "6":
                try:
                    opcion_6()
                except ValueError:
                    print("-------------------------")
                    print("|No hay tareas completas|")
                    print("-------------------------")
            #flujo para mostrar todas las tareas
            case "7":
                opcion_7()    
            case "8":
                try:
                    opcion_7()
                    titulo=title()
                    opcion_8(titulo)
                    print("-------------------------------")
                    print("|Tarea correctamente eliminada|")
                    print("-------------------------------")
                except ValueError:
                    print("------------------------------")
                    print("|No se pudo eliminar la tarea|")
                    print("------------------------------")
            case "0":
                break
            case _:
                print("-------------------------")
                print("|elija una opcion valida|")
                print("-------------------------")
        input()
    conexion.close()
