"""
En este archivo se encuentran las funciones relativas al ejercicio nº2.
"""

from datetime import datetime
import pandas as pd


def df_nueva_variable(df_eje1):
    """
    Esta función se encarga de añadir una variable más al dataframe creado en
    el ejercicio 1.2. La función se ha diseñado de tal forma, que la variable
    refleje el número de días que la serie ha estado en emisión.

    Parámetros de entrada:
    - df_eje1 (pandas df) -- esta variable se corresponde con el dataframe del
    ejercicio 1.2.

    Parámetros de salida:
    - df_eje1 (pandas df) -- el nuevo dataframe con la variable añadida.
    - df_final (pandas df) -- el dataframe ordenado de manera descendente (de 
    mayor a menor número de días de serie/doc/pelicula emitida)
    """

    # creamos una lista donde guardaremos los dias
    lista_dias = []
    for _, row in df_eje1.iterrows():
        if pd.isna(row['first_air_date']) or pd.isna(row['last_air_date']):
            lista_dias.append("-300000")
        else:
            a = row['first_air_date']
            b = row['last_air_date']
            fecha1 = datetime.strptime(a, "%Y-%m-%d")
            fecha2 = datetime.strptime(b, "%Y-%m-%d")
            dias_emision = fecha2 - fecha1
            dias_emision = dias_emision.days # esto es un "int"
            if dias_emision < 0:
                row['first_air_date'] = b
                row['last_air_date'] = a
                lista_dias.append(abs(dias_emision))
            else:
                lista_dias.append(dias_emision)

    # ahora convertimos la lista de strings a una lista de ints, para poder
    # ordenar el dataframe y  mostrar los 10 registros con más días emitidos
    lista_dias = list(map(int, lista_dias))

    # añadimos una columna vacía en el dataframe con el nombre: "air_days"
    # la columna la vamos a añadir despues de la columna: "last_air_date"
    # para ello necesitamos el índice de la columna "last_air_date" + 1.
    idx_last_air_date = df_eje1.columns.get_loc("last_air_date")
    df_eje1.insert(idx_last_air_date+1, 'air_days', lista_dias)

    # ahora ordenamos el dataframe según el número de días en emisión
    df_final = df_eje1.sort_values(by = 'air_days', ascending = False)
    return df_eje1, df_final


def diccionario2_2(df_eje1):
    """
    Esta función se encarga de dar solución al ejercicio 2.2. Por lo tanto,
    en esta función se crea un diccionario ordenado, dónde la clave será el
    nombre de la serie y su valor será (homepage y poster_path).

    Parámetros de entrada:
    - df_eje1 (pandas df) -- esta variable se corresponde con el dataframe del
    ejercicio 1.2.

    Parámetros de salida:
    - diccionario (dict) -- este es el diccionario con las caracteríticas que
    se nos pide en el enunciado.
    """

    diccionario = {}
    i = 0
    for _, row in df_eje1.iterrows():
        if pd.isna(row['homepage']) or pd.isna(row['poster_path']):
            key = row['name']
            if key not in diccionario:
                diccionario[key] =[]
            diccionario[key].append('NOT AVAILABLE')

        else:
            key = row['name']
            if key not in diccionario:
                diccionario[key] =[]
            home = row['homepage']
            poster = row['poster_path']
            # print(f"El tipo de home {i} es: {type(home)} y es: {home}")
            # print(f"El tipo de poster es: {type(poster)} y es: {poster}")
            web = home + '' + poster
            i += 1
            diccionario[key].append(web)

    return diccionario
