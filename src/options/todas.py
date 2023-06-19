from ..bd_connect import *
from ..func.funciones import *
def opcion_7():
    resultado = todas()
    print("")
    try:
        imprimir_tuplas(resultado)
        return 1
    except ValueError:
        print("-------------------")
        print("|No existen tareas|")
        print("-------------------")