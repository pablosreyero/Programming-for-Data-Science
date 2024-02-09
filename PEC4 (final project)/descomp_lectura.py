"""
En este archivo se encuentran las funciones relativas al ejercicio nº1.
"""

import os
import zipfile
import tarfile
import time
import csv
import pandas as pd


def descompresion(ruta):
    """
    Esta función se encarga de descomprimir los archivos contenidos en la ruta 
    que la función recibe como parámetro.

    Argumento de entrada:
    - ruta (string) -- contiene la ruta con el nombre del archivo que se
    quiere descomprimir.
    """

    # Obtener la extensión del archivo
    # se ha optado por "os.path.splitext" para extraer la extensión, porque
    # "endswith()" no soporta extensiones dobles.

    _, extension = os.path.splitext(ruta.lower())

    if extension in (".tar.gz",  ".tgz"):
        # Descomprimir archivo tar.gz
        with tarfile.open(ruta, 'r:gz') as tar_ref:
            tar_ref.extractall(os.path.dirname(ruta))
        nombre_archivo = os.path.basename(ruta)
        print(f"Archivo {nombre_archivo} descomprimido correctamente")
        booleano = True

    elif extension == ".zip":
        # Descomprimir archivo zip
        with zipfile.ZipFile(ruta, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(ruta))
        nombre_archivo = os.path.basename(ruta)
        print(f"Archivo {nombre_archivo} descomprimido correctamente")
        booleano = True

    else:
        print(f"Error: El archivo {ruta} no es ni zip ni tar.gz, o no existe")
        booleano = False

    return booleano


def lectura_pandas(ruta):
    """
    Esta función se encarga de leer los archivos csv descomprimidos y de
    integrarlos en el mismo dataframe, usando como clave la columna "id", con 
    la ayuda de la librería "pandas".

    Parámetros de entrada:
    - ruta (string) -- contiene la dirección dónde se supone que se han
    descomprimido los archivos.

    Parámetros de salida:
    - df_final (pandas df) -- se corresponde con el dataframe que se ha creado
    a partir de la fusión de los 3 df individuales correspondientes a cada uno 
    de los 2 archivos.
    - tiempo (float) -- el tiempo transcurrido desde la lectura de los csvs
    hasta su fusión en un solo dataframe.
    """

    # nos quedamos solo con la ruta donde tenemos que mirar.
    ruta = os.path.dirname(ruta)

    # ahora leemos los archivos que hay en el directorio
    archivos = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(".csv"):
            archivos.append(archivo)
    # print(f"Esta es la lista de archivos: {archivos}\n")

    # inicializamos el dataframe donde guardaremos los tres
    df_final = pd.DataFrame()

    # creamos una lista de las columnas IDs para comprobar que son iguales
    cols_id = []

    # ya tenemos los archivos en una lista, ahora hay que leerlos y fusionarlos
    t_inicio = time.time()
    for datafr in archivos:
        df_i = pd.read_csv(ruta+"/"+datafr)
        # print(f'El df {datafr} tiene {len(df_i)} filas y {df_i.shape[1]} cols')
        col_id = list(df_i["id"])
        cols_id.append(col_id)

        # cogemos columnas no repetidas
        if 'id' in df_final:
            df_final = pd.concat([df_final, df_i.iloc[:, 1:]], axis=1)
        else:
            df_final = pd.concat([df_final, df_i], axis=1)

    # ahora calculamos el tiempo que ha transcurrido
    t_final = time.time()
    t_total = t_final - t_inicio

    return df_final, t_total


def lectura_csvs(ruta):
    """
    Esta función se encarga de leer los archivos csv descomprimidos y de
    integrarlos en un mismo diccionario, usando como clave la columna "id", 
    con la ayuda de la librería "csv".

    Parámetros de entrada:
    - ruta (string) -- contiene la dirección dónde se supone que se han
    descomprimido los archivos.

    Parámetro de salida:
    - dict_final (dict) -- se trata del diccionario obtenido, tras leer los 3
    csvs con la ayuda de la librería "csv" de python. Dicho diccionario tiene
    como claves los IDs y como valores, diccionarios anidados con el resto de
    columnas de cada uno de los 3 csvs.
    - tiempo (float) -- el tiempo transcurrido desde la lectura de los csvs
    hasta su fusión en un solo dataframe.
    """

    # nos quedamos solo con la ruta donde tenemos que mirar.
    ruta = os.path.dirname(ruta)

    # ahora leemos los archivos que hay en el directorio
    archivos = []
    for archivo in os.listdir(ruta):
        if archivo.endswith(".csv"):
            archivos.append(archivo)

    # inicializamos el diccionario final
    dict_final = {}
    t_inicio = time.time()
    for archivo in archivos:
        ruta_archivo = ruta + '/' + archivo
        with open(ruta_archivo, 'r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)

            # Iteramos sobre las filas del csv
            for row in reader:
                # extraemos el ID
                id_col = row['id']

                # Si no exsite ID, creamos una clave con dicho ID
                if id_col not in dict_final:
                    dict_final[id_col] = {}

                # Añadimos las cols y sus valores al dict anidado
                for col, val in row.items():
                    if col != 'id': # no añadir la clave id
                        dict_final[id_col][col] = val

    # Medimos el tiempo al acabar la ejecución de la función
    t_final = time.time()

    return dict_final, t_final - t_inicio
