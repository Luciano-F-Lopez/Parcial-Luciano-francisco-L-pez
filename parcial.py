
from funciones_parcial import *
from menu_parcial import *

#1



while True:
    match menu_01():
        case"1":
            bicicletas = cargar_csv("bicicletas.csv")     
        case"2":
            print(bicicletas)
        case"3":
            x = bicileta_random(bicicletas)
            print(x)
        case"4":
            ganador = ganador_bicicleta(bicicletas)
            print(ganador)
        case"5":
            bicicletasPLAYERA = filtrar_listas(lambda tipo:(tipo["tipo"] == "PLAYERA"),bicicletas)
            bicicletasBMX = filtrar_listas(lambda tipo:(tipo["tipo"] == "BMX"),bicicletas)
            bicicletas2MTB = filtrar_listas(lambda tipo:(tipo["tipo"] == "MTB"),bicicletas)
            bicicletas2PASEO = filtrar_listas(lambda tipo:(tipo["tipo"] == "PASEO"),bicicletas)

            guardar_archivo_csv(bicicletasPLAYERA,"playera.csv")
            guardar_archivo_csv(bicicletasBMX,"BMX.csv")
            guardar_archivo_csv(bicicletas2MTB,"MTB.csv")
            guardar_archivo_csv(bicicletas2PASEO,"PASEO.csv")
            
        case"6":
            
            bici_a_eleccion = input("ingrese un tipo de bici: ")
            promedio = promedio_tipo_bici(x, bici_a_eleccion)
            print(f"el promedio de tiempo de la bici seleccionada es:\n {bici_a_eleccion}: {promedio}\n")
            
        case"7":
            
            playera = ordenar_ascendente_por_tiempo(bicicletasPLAYERA)
            bmx = ordenar_ascendente_por_tiempo(bicicletasBMX)
            paseo = ordenar_ascendente_por_tiempo(bicicletas2PASEO)
            mtb = ordenar_ascendente_por_tiempo(bicicletas2MTB)

            print(f"Playera:  {playera} \n\nBmx: {bmx} \n\nPaseo:  {paseo} \n\nMtb:  {mtb}")
        case"8":
            playera = ordenar_ascendente_por_tiempo(bicicletasPLAYERA)
            bmx = ordenar_ascendente_por_tiempo(bicicletasBMX)
            paseo = ordenar_ascendente_por_tiempo(bicicletas2PASEO)
            mtb = ordenar_ascendente_por_tiempo(bicicletas2MTB)

            guardar_archivo_json("lista_playera.json",playera)
            guardar_archivo_json("lista_bmx.json",bmx)
            guardar_archivo_json("lista_paseo.json",paseo)
            guardar_archivo_json("lista_mtb.json",mtb)
        case"9":
            break
    pausar()
print("Fin del programa")








