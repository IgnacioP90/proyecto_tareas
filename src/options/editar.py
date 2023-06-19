from ..bd_connect import *
from ..func.funciones import *
def opcion_3(titulo,opcion=None):
    comprobar=conexion.execute("SELECT * FROM tareas WHERE titulo=?" , (titulo,))
    esto=comprobar.fetchone()
    if esto:
        match opcion:
            # opcion para editar el titulo
            case "1":    
                variable=input("Ingrese un nuevo titulo: ")
            # opcion para editar la descripcion
            case "2":                                        
                variable=input("Ingrese una nueva descripcion: ")
                # opcion para editar la fecha
            case "3":                                         
                variable=fecha_vencimiento(opcion)
            # opcion para editar la prioridad
            case "4":                                         
                variable=prioridad()
        e = editar_tarea(titulo, opcion, variable)
        return e
    else:
        return 2 # aca es donde compruebo si existe la tarea
    