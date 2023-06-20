from ..bd_connect import *
from ..func.funciones import *
def opcion_3(titulo,opcion):
    comprobar=conexion.execute("SELECT * FROM tareas WHERE titulo=?" , (titulo, ))
    esto=comprobar.fetchone()
    if esto!=None:
        match opcion:
            # opcion para editar el titulo
            case "1":    
                variable=title()
            # opcion para editar la descripcion
            case "2":                                        
                variable=descript()
                # opcion para editar la fecha
            case "3":                                         
                variable=fecha_vencimiento(opcion)
            # opcion para editar la prioridad
            case "4":                                         
                variable=prioridad()
        e = editar_tarea(titulo, variable, opcion)
        return e
    else:
        return 2 # aca es donde compruebo si existe la tarea
    