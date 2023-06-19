from bd_connect import *
from funciones import *
def opcion_7():
    resultado = todas()
    print("")
    print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
    for filas in resultado:
        print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
    print("")