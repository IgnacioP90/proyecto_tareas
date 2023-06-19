from ..bd_connect import *
from ..func.funciones import *
def opcion_7():
    resultado = todas()
    print("")
    if resultado:
        imprimir_tuplas(resultado)
        return 1
    else:
        print("-------------------")
        print("|No existen tareas|")
        print("-------------------")