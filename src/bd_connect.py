import sqlite3

conexion = sqlite3.connect("./src/bd1.db")
cursor = conexion.cursor()

try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS tareas (
                        titulo TEXT PRIMARY KEY,
                        descripcion TEXT,
                        fec_ven TEXT,
                        prioridad TEXT,
                        estado TEXT,
                        limite INT
                    )""")
except sqlite3.Error as e:
    print("Hubo un error al crear la tabla:", e)






