from ..bd_connect import *
from ..func.funciones import *
def opcion_8(titulo):
    query=conexion.execute("SELECT * FROM tareas WHERE titulo=?" , (titulo, ))
    resultado=query.fetchone()
    delete(resultado,titulo)