from ..bd_connect import *
from ..func.funciones import *
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
        print("-------------------------")
        print("Tarea agregada con exito!")
        print("-------------------------")
    except sqlite3.OperationalError:
        print("-------------------------------------")
        print("no se ha podido realizar la operacion")
        print("-------------------------------------")
        