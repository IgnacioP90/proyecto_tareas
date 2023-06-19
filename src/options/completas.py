from ..bd_connect import *
from ..func.funciones import *
def opcion_6():
    resultado = tareas_completas()
    print("")
    print("{:<25} | {:<30} | {:<22} | {:<10} | {:<10}".format("titulo", "descripcion", "fecha de vencimiento", "prioridad", "estado"))
    for filas in resultado:
        print("{:<25} | {:<30} | {:<22} | {:<10} | {:<10}".format(filas[0], filas[1], filas[2], filas[3], filas[4]))
    print("")