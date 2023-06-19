from bd_connect import *
def agregar_tarea(titulo,desc,fec_venc,prioridad):
    conexion.execute("insert into tareas (titulo, descripcion, fec_ven, prioridad, estado) values (?,?,?,?,?)" , (titulo,desc,fec_venc,prioridad,"pendiente"))
    conexion.commit()
    
def completar_tarea(titulo): 
        resultado=conexion.execute("SELECT * FROM tareas WHERE titulo=?", (titulo,))
        status=resultado.fetchone()
        if(status[4]=='pendiente'):
            conexion.execute("UPDATE tareas SET estado='completa' WHERE titulo=?", (titulo,))
            conexion.commit()
        return status
   
def tareas_pendientes():
    result=conexion.execute("SELECT * FROM tareas WHERE estado='pendiente'")
    resultado=result.fetchall()
    return resultado

def editar_tarea(titulo, opcion, variable):
    #selecciono la fila que tenga el mismo titulo que traje a la funcion, luego pregunto si esta en estado pendiente y ahi si la edito,
    #sino no hago nada
    tarea=conexion.execute("SELECT * FROM tareas WHERE titulo=?" , (titulo,))
    data=tarea.fetchone()
    if(data[4]=='pendiente'):
        match (opcion):
            case "1": 
                conexion.execute("UPDATE tareas SET titulo=? WHERE titulo=?" , (variable,titulo))
                conexion.commit()
            case "2": 
                conexion.execute("UPDATE tareas SET descripcion=? WHERE titulo=?" , (variable,titulo))
                conexion.commit()
            case "3": 
                conexion.execute("UPDATE tareas SET fec_ven=? WHERE titulo=?" , (variable,titulo))
                conexion.commit()
            case "4":
                conexion.execute("UPDATE tareas SET prioridad=? WHERE titulo=?" , (variable,titulo))
                conexion.commit()
    else:
        return 1 # retorno una bandera para hacer una comprobacion

def tareas_completas():
    result=conexion.execute("SELECT * FROM tareas WHERE estado='completa'")
    resultado=result.fetchall()
    return resultado

def buscar_tarea(variable, opcion):
    match opcion:
        case "1":
            result=conexion.execute("SELECT * FROM tareas WHERE titulo=?", (variable, ))
            algo=result.fetchall()
            return algo
        case "2":
            result=conexion.execute("SELECT * FROM tareas WHERE fec_ven=?", (variable, ))
            algo=result.fetchall()
            return algo
        case "3":
            result=conexion.execute("SELECT * FROM tareas WHERE prioridad=?", (variable, ))
            algo=result.fetchall()
            return algo

def todas():
    result=conexion.execute("SELECT * FROM tareas")
    resultado=result.fetchall()
    return resultado

def convertir(fec_venc):   # convierto la variable fec_venc a datetime, a menos que ya sea 
    if type(fec_venc) != datetime: 
        vence = datetime.strptime(fec_venc, "%Y-%m-%d %H:%M:%S")
    else:
        vence = fec_venc
    return vence
# funcion para ingresar las fechas en las distintas opciones
def fecha_vencimiento(eleccion=None): # eleccion=None lo use porque hay veces que mando un parametro y otras veces no
    while(True):
        try:
            dia=int(input("ingrese dia en formato DD: "))
            mes=int(input("ingrese mes en formato MM: "))
            anio=int(input("ingrese año en formato YYYY: "))    # ingreso la fecha para luego convertirla a formato datetime
            fecha_hora_str=f"{anio}-{mes}-{dia} 00:00:00"  # todo lo que ingrese, lo transformo a string
            fec_venc=datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")  # ahora se convierte a formato datetime con el metodo strptime
            fec_convert=convertir(fec_venc)
            if fecha_actual>fec_convert and eleccion==None:
                print("ha ingresado una fecha anterior a la fecha actual")
            else:
                break
        except:
            print("Ha ingresado una fecha erronea.")
    return fec_venc
# actualiza las tareas, cuando la fecha de vencimiento de la tarea, sobrepasa a la tarea actual, cada una de ellas tendra el estado a vencida, estando en estado pendiente
def actualizar(fecha_actual):
    estado=conexion.execute("SELECT fec_ven, estado FROM tareas WHERE estado='pendiente'")
    status=estado.fetchall()
    for stat in status:
        fecha = datetime.strptime(stat[0], "%Y-%m-%d %H:%M:%S")
        if fecha<=fecha_actual and stat[1]!='completa':
            conexion.execute("UPDATE tareas SET estado='vencida' WHERE fec_ven=?", (fecha,))
            conexion.commit()
        
# valido la variable prioridad                
def prioridad():
    while True:
        prioridad=input("ingrese una prioridad (alta,media,baja): ")
        if(prioridad != "alta" and prioridad != "media" and prioridad != "baja"):
            print("Ingrese una prioridad correcta por favor")
        else:
            break
    prioridad=prioridad.upper()
    return prioridad
def vencimientos():
    a=0
    b=0
    todo=todas()
    actualizar(fecha_actual)
    for tareas in todo:
        s=convertir(tareas[2]) # Debo convertirlo a tipo datetime porque desde la base de datos esta en tipo str
        vencidas=s-fecha_actual #resto la fecha actual con cada una de las fechas que aparecen en la base de datos
        tareas_por_vencer=vencidas.days*24+vencidas.seconds // 3600 # convierto la fecha en numeros, el equivalente a las horas.
        if(tareas[4] == 'vencida'):
            a+=1
        if(tareas_por_vencer<=24 and tareas[4] == 'pendiente'):  
            b+=1
    return a,b