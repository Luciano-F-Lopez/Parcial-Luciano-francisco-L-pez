from funciones_parcial import *
bicicletas = leer_archivo_csv("bicicletas.csv")

bicicletasPLAYERA = filtrar_listas(lambda tipo:(tipo["tipo"] == "PLAYERA"),bicicletas)
# playera = bicicletas_ordenadas_tipo_ascendente(bicicletasPLAYERA,"PLAYERA")
x = bicileta_random(bicicletasPLAYERA)

def ordenar_por_tiempo(bicicletas):
    """
    Ordena una lista de diccionarios por el campo 'tiempo' en orden ascendente.

    Parámetros:
    bicicletas (list): Lista de diccionarios, cada uno representando una bicicleta.

    Retorna:
    list: Lista de diccionarios ordenada por el campo 'tiempo'.
    """
    return sorted(bicicletas, key=lambda x: x['tiempo'])

def ordenar_por_tiempo_2(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lista[j]['tiempo'] < lista[min_idx]['tiempo']:
                min_idx = j
        # Intercambiar elementos
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    
    return lista

bbbb = ordenar_por_tiempo_2(x)

print(bbbb)

print("-.-----------------------------------------------------------------------")

aaa = ordenar_por_tiempo(bicicletasPLAYERA)
print(aaa)