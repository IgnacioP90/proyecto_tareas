from bd_connect import *
from funciones import *
def opcion_4(titulo):
    done=completar_tarea(titulo)
    print("")
    match done[4]:
        case "pendiente":
            print("A continuacion, se mostrara la tarea completa: ")
            print("")
            print("{:<15} | {:<30} | {:<22} | {:<10} | {:<10}".format(done[0],done[1],done[2],done[3],done[4]))
            print("")
        case 'completa':
            print("------------------------------")
            print("|La tarea ya estaba completa.|")
            print("------------------------------")
        case 'vencida':
            print("-----------------------------")
            print("|La tarea ya estaba vencida.|")
            print("-----------------------------")     