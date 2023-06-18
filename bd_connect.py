import sqlite3
from datetime import *
fecha_actual = datetime.now()
conexion=sqlite3.connect("bd1.db")
try:
    conexion.execute(f"""CREATE TABLE tareas (
                                titulo TEXT PRIMARY KEY,
                                descripcion TEXT,
                                fec_ven TEXT,
                                prioridad TEXT,
                                estado TEXT
                        )""")
    print("Base de datos creada con exito")
except sqlite3.Error as e:
    if ("table tareas already exists" in str(e)):
        print("BIENVENIDO AL GESTOR DE TAREAS!")
    else:
        print("hubo un error al crear la tabla: ", e)






