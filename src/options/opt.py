from ..bd_connect import *
from ..func.funciones import *
#opcion para agregar tarea

def opcion_1():
    a=0
    comprobar=conexion.execute("SELECT * FROM tareas")
    array=comprobar.fetchall()
    titulo=title()
    for tit in array:
        if tit[0]==titulo:
            a=1
            break
    if a==0:
        desc=descript()
        print("ahora debera ingresar una fecha de vencimiento:")
        fec_venc=fecha_vencimiento() # Funcion fecha de vencimiento donde ingreso la fecha y la valido
        priori=prioridad() # Cree una funcion prioridad para que solo haya 3, alta media o baja
        print("Desea agregar dias al vencimiento? s/n")
        select=input().lower()
        if(select=="s"):
            while True:
                numero=int(input("Ingrese la cantidad de dias, limite maximo, 7 dias: "))
                if numero>7 and numero<0:
                    print("ingrese un numero correcto por favor.")
                else:
                    break
        else:
            numero=0
    else:
        raise KeyboardInterrupt
    try:
        agregar_tarea(titulo,desc,fec_venc,priori,numero)
        print("---------------------------")
        print("|Tarea agregada con exito!|")
        print("---------------------------")
    except sqlite3.OperationalError:
        print("---------------------------------------")
        print("|No se ha podido realizar la operacion|")
        print("---------------------------------------")
        
#opcion para buscar tarea

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
    
# opcion para editar tarea

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
    
#opcion para completar tarea
   
def opcion_4(titulo):
    done=completar_tarea(titulo)  
    print("")
    match done[4]:
        case "pendiente":
            print("A continuacion, se mostrara la tarea completa: ")
            print("")
            print("{:<25} | {:<30} | {:<22} | {:<10} | {:<10}".format(done[0],done[1],done[2],done[3],done[4]))
            print("")
        case 'completa':
            print("------------------------------")
            print("|La tarea ya estaba completa.|")
            print("------------------------------")
        case 'vencida':
            print("-----------------------------")
            print("|La tarea ya estaba vencida.|")
            print("-----------------------------")
             
#muestra todas las tareas pendientes 

def opcion_5():
    resultado = tareas_pendientes()
    imprimir_tuplas(resultado)
                   
#muestra todas las tareas completas 

def opcion_6():
    resultado = tareas_completas()
    imprimir_tuplas(resultado)
    
#muestra todas las tareas

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
        
#elimina una tarea  
      
def opcion_8(titulo):
    query=conexion.execute("SELECT * FROM tareas WHERE titulo=?" , (titulo, ))
    resultado=query.fetchone()
    delete(resultado,titulo)