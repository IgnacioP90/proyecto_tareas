from datetime import *
fecha=datetime.now()
dia=int(input("dia: "))
mes=int(input("mes: "))
anio=int(input("anio: "))
hora=0
minuto=0
segundo=0
for hora in range(24):
    for minuto in range(60):
        for segundo in range(60):
            hora_str=str(hora)
            minuto_str=str(minuto)
            segundo_str=str(segundo)
            fecha_str=f"{anio}-{mes}-{dia} {hora_str}:{minuto_str}:{segundo_str}"
            fecha_v=datetime.strptime(fecha_str, "%Y-%m-%d %H:%M:%S")
            if fecha==fecha_v:
                print(fecha , "es igual ", fecha_v)
                break
            else:
                print("hola")
                break