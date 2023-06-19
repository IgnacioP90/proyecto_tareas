from ..bd_connect import *
from ..func.funciones import *
def opcion_2(eleccion, titulo=None, fec_venc=None, priori=None):
    match eleccion:
        case "1":
            tupla=buscar_tarea(titulo, eleccion)
            if not tupla:
                raise ValueError
            else:
                imprimir_tuplas(tupla)
        case "2":
            tupla=buscar_tarea(fec_venc, eleccion)
            if not tupla:
                raise ValueError
            else:
                imprimir_tuplas(tupla)
        case "3":
            tupla=buscar_tarea(priori, eleccion)
            if not tupla:
                raise ValueError
            else:
                imprimir_tuplas(tupla)
    if tupla:
        return 1