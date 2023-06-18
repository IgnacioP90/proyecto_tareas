from bd_connect import *
from funciones import *
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
                            array=buscar_tarea(titulo, eleccion)
                            print("")
                            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
                            for filas in array:
                                print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
                            print("")
                        except:
                            print("-----------------------------------------")
                            print("|No se encontro una tarea con ese titulo|")
                            print("-----------------------------------------")
                    # buscar tarea por fecha de vencimiento
                    case "2":
                        print("Ingrese la tarea a buscar por fecha de vencimiento: ")
                        fec_venc=fecha_vencimiento(eleccion) 
                        try:                  
                            array=buscar_tarea(fec_venc, eleccion)
                            print("")
                            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
                            if array:
                                
                                for filas in array:
                                        print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
                                print("")
                            else:
                                print("no")
                        except:
                            print("----------------------------------------")
                            print("|No se encontro una tarea con esa fecha|")
                            print("----------------------------------------")
                    # buscar tarea por prioridad
                    case "3":
                        priori=prioridad()
                        try:
                            array=buscar_tarea(priori, eleccion)
                            print("")
                            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
                            for filas in array:
                                print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
                            print("")
                        except:
                            print("----------------------------------------")
                            print("|No se encontro una tarea con esa fecha|")
                            print("----------------------------------------")
            # flujo para editar una tarea     
            case "3":
                titulo=input("Ingrese titulo de la tarea: ")
                print("")
                opcion=input(f"""elija una de las opciones a editar:
                                1) titulo
                                2) descripcion
                                3) fecha de vencimiento
                                4) prioridad
    : """)
                match opcion:
                    # opcion para editar el titulo
                    case "1":    
                        variable=input("Ingrese un nuevo titulo: ")
                    # opcion para editar la descripcion
                    case "2":                                        
                        variable=input("Ingrese una nueva descripcion: ")
                    # opcion para editar la fecha
                    case "3":                                         
                        fec_venc=fecha_vencimiento(opcion)
                    # opcion para editar la prioridad
                    case "4":                                         
                        variable=prioridad()
                e = editar_tarea(titulo, opcion, variable)
                if e:
                    print("--------------------------------------------------")
                    print("|No se puede editar una tarea completa o vencida.|")
                    print("--------------------------------------------------")
            #flujo para marcar una tarea como completa
            case "4":
                try:
                    titulo=input("Ingrese la tarea a completar: ")
                    done=completar_tarea(titulo)
                    print("")
                    match done[4]:
                        case "pendiente":
                            print("A continuacion, se mostrara la tarea completa: ")
                            print("")
                            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(done[0],done[1],done[2],done[3],done[4]))
                            print("")
                        case 'completa':
                            print("------------------------------")
                            print("|La tarea ya estaba completa.|")
                            print("------------------------------")
                        case 'vencida':
                            print("-----------------------------")
                            print("|La tarea ya estaba vencida.|")
                            print("-----------------------------")     
                except TypeError:
                    print("---------------------")
                    print("|La tarea no existe.|")
                    print("---------------------")
            # flujo para mostrar las tareas pendientes
            case "5":
                resultado = tareas_pendientes()
                if len(resultado)>0:
                    print("")
                    print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
                    for filas in resultado:
                        print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
                    print("")
                else:
                    print("--------------------------")
                    print("|No hay tareas pendientes|")
                    print("--------------------------")
            #flujo para mostrar las tareas que ya estan completas
            case "6":
                resultado = tareas_completas()
                if len(resultado)>0:
                    print("")
                    print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
                    for filas in resultado:
                        print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
                    print("")
                else:
                    print("-------------------------")
                    print("|No hay tareas completas|")
                    print("-------------------------")
            #flujo para mostrar todas las tareas
            case "7":
                resultado = todas()
                print("")
                print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
                for filas in resultado:
                    print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
                print("")
            case "0":
                break
            case _:
                print("-------------------------")
                print("|elija una opcion valida|")
                print("-------------------------")
        input()
    conexion.close()
