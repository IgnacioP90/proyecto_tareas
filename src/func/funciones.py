from ..bd_connect import *
from datetime import *

fecha_actual = datetime.now()
def agregar_tarea(titulo, desc, fec_venc, prioridad, numero):
    conexion.execute(
        "INSERT INTO tareas (titulo, descripcion, fec_ven, prioridad, estado, limite) VALUES (?,?,?,?,?,?)",
        (titulo, desc, fec_venc, prioridad, 'pendiente', numero))
    conexion.commit()

def completar_tarea(titulo):
    resultado = conexion.execute("SELECT * FROM tareas WHERE titulo=?", (titulo,))
    status = resultado.fetchone()
    if status:
        if (status[4] == 'pendiente'):
            conexion.execute("UPDATE tareas SET estado='completa' WHERE titulo=?", (titulo,))
            conexion.commit()
        return status
    else:
        return None


def tareas_pendientes():
    result = conexion.execute("SELECT * FROM tareas WHERE estado='pendiente'")
    resultado = result.fetchall()
    if resultado:
        return resultado
    else:
        return None


def editar_tarea(titulo, variable, opcion):
    # selecciono la fila que tenga el mismo titulo que traje a la funcion, luego pregunto si esta en estado pendiente y ahi si la edito,
    # sino no hago nada
    tarea = conexion.execute("SELECT * FROM tareas WHERE titulo=?", (titulo,))
    data = tarea.fetchone()
    if (data[4] != 'completa'):
        match (opcion):
            case "1":
                conexion.execute("UPDATE tareas SET titulo=? WHERE titulo=?", (variable, titulo))
                conexion.commit()
            case "2":
                conexion.execute("UPDATE tareas SET descripcion=? WHERE titulo=?", (variable, titulo))
                conexion.commit()
            case "3":
                conexion.execute("UPDATE tareas SET fec_ven=? WHERE titulo=?", (variable, titulo))
                conexion.commit()
            case "4":
                conexion.execute("UPDATE tareas SET prioridad=? WHERE titulo=?", (variable, titulo))
                conexion.commit()
        return data
    else:
        return 1  # retorno una bandera para hacer una comprobacion


def tareas_completas():
    result = conexion.execute("SELECT * FROM tareas WHERE estado='completa'")
    resultado = result.fetchall()
    if resultado:
        return resultado
    else:
        return None


def buscar_tarea(variable, opcion):
    algo = None
    match opcion:
        case "1":
            result = conexion.execute("SELECT * FROM tareas WHERE titulo=?", (variable,))
            algo = result.fetchall()
            return algo
        case "2":
            result = conexion.execute("SELECT * FROM tareas WHERE fec_ven BETWEEN ? AND ?", (variable[0], variable[1]))
            algo = result.fetchall()
            return algo
        case "3":
            result = conexion.execute("SELECT * FROM tareas WHERE prioridad=?", (variable,))
            algo = result.fetchall()
            return algo
    if not algo:
        return None
def busqueda(texto):
    res = conexion.execute("SELECT * FROM tareas WHERE titulo=?", (texto,))
    result = res.fetchone()
    if result:
        return result
    else:
        return None



def todas():
    result = conexion.execute("SELECT * FROM tareas")
    resultado = result.fetchall()
    if resultado:
        return resultado
    else:
        return None


def convertir(fec_venc, eleccion=None):  # convierto la variable fec_venc a datetime, a menos que ya sea
    if type(fec_venc) != datetime:
        vence1 = None
        if eleccion == "2":
            vence = datetime.strptime(fec_venc[0], "%Y-%m-%d %H:%M:%S")
            vence1 = datetime.strptime(fec_venc[1], "%Y-%m-%d %H:%M:%S")
            return vence, vence1
        else:
            vence = datetime.strptime(fec_venc, "%Y-%m-%d %H:%M:%S")
    else:
        vence = fec_venc
    return vence


# funcion para ingresar las fechas en las distintas opciones
def fecha_vencimiento(fecha, hym,eleccion=None):  # eleccion=None lo use porque hay veces que mando un parametro y otras veces no
    fec_venc = None
    fecha_actual = datetime.now()

    # ingreso la fecha para luego convertirla a formato datetime
    if eleccion == "2":
        fecha_str = fecha.toString("yyyy-MM-dd")
        fecha_hora_str2 = f"{fecha_str} 00:00:00"
        fecha_hora_str1 = f"{fecha_str} 23:59:59"
        fecha_hora_str = fecha_hora_str2, fecha_hora_str1
        fec_venc = convertir(fecha_hora_str, eleccion)
    else:
        fecha_str = fecha.toString("yyyy-MM-dd")
        hora_str = hym.toString("HH:mm:ss")
        fecha_hora_str = fecha_str + " " + hora_str
        fec_venc = convertir(fecha_hora_str, eleccion)

        if fec_venc <= fecha_actual and eleccion is None:
            raise TypeError

    return fec_venc


# actualiza las tareas, cuando la fecha de vencimiento de la tarea, sobrepasa a la tarea actual, cada una de ellas tendra el estado a vencida, estando en estado pendiente
def actualizar(fecha_actual):
    try:
        conexion.execute("SELECT limite FROM tareas")
    except sqlite3.OperationalError:
        conexion.execute("ALTER TABLE tareas ADD limite INT")
        conexion.commit()
    estado = conexion.execute("SELECT titulo, fec_ven, estado, limite FROM tareas")
    status = estado.fetchall()
    for stat in status:
        if (stat[3] == None):
            conexion.execute("UPDATE tareas SET limite=0 WHERE limite IS NULL")
            conexion.commit()
        fecha = convertir(stat[1])
        limite = stat[3]
        limit = cantidad_dias(fecha, limite)
        vencidas = limit - fecha_actual
        tareas_por_vencer = vencidas.days * 24 + vencidas.seconds // 3600

        if tareas_por_vencer <= 0 and stat[2] == 'pendiente':
            conexion.execute("UPDATE tareas SET estado='vencida' WHERE titulo=? and fec_ven=?", (stat[0], fecha))
            conexion.commit()

        if limit >= fecha_actual and stat[2] == 'vencida':
            conexion.execute("UPDATE tareas SET estado='pendiente' WHERE titulo=? and fec_ven=?", (stat[0], fecha))
            conexion.commit()






def vencimientos():
    a = 0
    b = 0
    c = []
    d = []
    actualizar(fecha_actual)
    todo = todas()
    if todo:
        for tareas in todo:
            s = convertir(tareas[2])  # Debo convertirlo a tipo datetime porque desde la base de datos esta en tipo str
            limit = cantidad_dias(s, tareas[5])  # actualizo la fecha de vencimiento para que me muestre la fecha sumado a los dias que se le agrega al vencimiento, seria, sumando fecha de vencimiento y limite
            vencidas = limit - fecha_actual  # resto la fecha actual con cada una de las fechas que aparecen en la base de datos
            tareas_por_vencer = vencidas.days * 24 + vencidas.seconds // 3600  # convierto la fecha en numeros, el equivalente a las horas.
            dias = vencidas.days
            horas = vencidas.seconds // 3600
            minutos = dias * 24 * 60 + vencidas.seconds // 60 % 60
            if (dias == 0):
                total = f"{horas} hs y {minutos} minutos"
            else:
                minutos = minutos % 60
                if (horas == 0):
                    total = f"{dias} dias y {minutos} minutos"
                else:
                    total = f"{dias} dias {horas} hs y {minutos} minutos"
            if (tareas[4] == 'vencida'):
                a += 1
            if (tareas_por_vencer <= 168 and tareas[4] == 'pendiente'):
                if (tareas_por_vencer <= 24 and tareas_por_vencer >= 0):
                    b += 1
                d.append(total)
                c.append(tareas[0])
        return a, b, c, d

def delete(titulo):
    query = conexion.execute("SELECT * FROM tareas WHERE titulo=?", (titulo,))
    resultado = query.fetchone()
    if resultado:
        conexion.execute("DELETE FROM tareas WHERE titulo=?", (titulo,))
        conexion.commit()
    else:
        raise ValueError



def cantidad_dias(fec_venc, limite):
    if limite == 0:
        return fec_venc
    dias = fec_venc + timedelta(days=limite)
    return dias


def mostrar_vencidas(vencidas=None, vencen_1=None, titulos=None, vencen=None):
    mensaje = ""
    if vencidas >= 1:
        mensaje += f"Tienes {vencidas} tarea(s) vencida(s). Tienes la posibilidad de editar la fecha si así lo deseas.\n"
    else:
        mensaje += "Felicidades, no tienes tareas vencidas!\n"
    mensaje += f"Cantidad de tareas que vencen en un día: {vencen_1}\n"
    mensaje += "Nombre de la(s) tarea(s) que vencerá(n) en una semana:\n"
    for titulo, vencimiento in zip(titulos, vencen):
        mensaje += f" Titulo: {titulo} - Vence en: {vencimiento}\n"
    return mensaje, vencen_1