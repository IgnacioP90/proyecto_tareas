from bd_connect import *
from funciones import *
def opcion_2(eleccion, titulo=None, fec_venc=None, priori=None):
    match eleccion:
        case "1":
            array=buscar_tarea(titulo, eleccion)
            print("")
            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
            for filas in array:
                print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
            print("")
        case "2":
            array=buscar_tarea(fec_venc, eleccion)
            print("")
            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
            for filas in array:
                print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
            print("")
        case "3":
            array=buscar_tarea(priori, eleccion)
            print("")
            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
            for filas in array:
                print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
            print("")