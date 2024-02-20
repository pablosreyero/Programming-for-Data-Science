"""
En este archivo se encuentran las funciones relativas al ejercicio nº3.
"""
import re
import pandas as pd


def buscar_palabras(cadena, valor):
    """
    Esta función se encarga de buscar las dos palabras deseadas.

    Parámetros de entrada:
    - cadena (str) -- se corresponde con la cadena de caractéres en la que
    queremos buscar si están o no las palabras deseadas.
    - valor (int) -- este valor puede tomar 1 o 2 como valor, si es 1, entonces
    se quiere buscar las palabras en overview, si es 2, buscaremos el idioma en
    el campo 'original_languages.

    Parámetros de salida:
    - booleano (bool) -- se corresponde con el booleano, resultado de la bús
    """

    if valor == 1:
        pauta = re.compile(r'\b(?:mystery|crime)\b', flags=re.IGNORECASE)
        booleano = bool(pauta.search(cadena))
    elif valor == 2:
        pauta = re.compile(r'\ben\b', flags=re.IGNORECASE)
        booleano = bool(pauta.search(cadena))

    return booleano


def series_31(df_eje1):
    """
    Esta función se encarga de obtener las series cuyo idioma original es el
    inglés y en cuyo resumen aparecen las palabras 'mystery' o 'crime' (sin
    tener en cuenta las mayúsculas ni las minúsculas)

    Parámetros de entrada:
    - df_eje1 (pandas df) -- esta variable se corresponde con el dataframe del
    ejercicio 1.2.

    Parámetros de salida:
    - lista_series (list) -- la lista con los nombres de las series que cumplen
    con el criterio de búsqueda mencionado antes.
    """
    # inicializamos la lista done meteremos los nombres de las series
    lista_series = []
    for _, row in df_eje1.iterrows():
        overview = isinstance(row['overview'], str)
        o_language = isinstance(row['original_language'], str)
        if overview and o_language:
            palabras_bool = buscar_palabras(row['overview'], valor=1)
            idioma_bool = buscar_palabras(row['original_language'], valor=2)
            if palabras_bool and idioma_bool:
                if row['name'] not in lista_series: # para evitar duplicados
                    lista_series.append(row['name'])

    return lista_series


def series_32(df_eje1):
    """
    Esta función se encarga de expedir una lista con las series que han
    empezado en 2023 y que han sido canceladas.

    Parámetros de entrada:
    - df_eje1 (pandas df) -- esta variable se corresponde con el dataframe del
    ejercicio 1.2.

    Parámetros de salida:
    - lista_series (list) -- la lista con los nombres de las series que cumplen
    con el criterio de búsqueda mencionado antes.
    """

    # primero obtenemos los posibles valores de la columna 'status'
    # valores_uni_status = sorted(df_eje1['status'].unique())

    # definimos las expresiones regulares que vamos a usar luego
    er1 = r'^2023'
    er2 = r'^(?:\d{2}-\d{2}|d{2}/\d{2})-2023'

    # como la palabra es Canceled, y no hay otra palabra canceled, no vamos a
    # hacer uso de expresiones regulares, porque no hace falta.
    lista_series = []
    for _, row in df_eje1.iterrows():
        fecha = row['first_air_date']
        estado = row['status']
        fecha_check = isinstance(fecha, str) # comprobamos tipo variable
        estado_check = isinstance(estado, str) # comprobamos tipo variable
        if fecha_check and estado_check:
            check_er1 = bool(re.match(er1, fecha)) # comprobamos coincidencia
            check_er2 = bool(re.match(er2, fecha)) # comprobamos coincidencia
            if check_er1 or check_er2:
                if estado == 'Canceled':
                    nombre_serie = row['name']
                    if nombre_serie not in lista_series:
                        lista_series.append(nombre_serie)

    return lista_series


def dataframe_33(df_eje1):
    """
    Esta función se encarga de crear un dataframe que contiene el nombre, el
    nombre original, las plataformas de emisión y las compañias de producción
    de los registros correspondientes a las series que tengan como lengua el
    japonés.

    Parámetros de entrada:
    - df_eje1 (pandas df) -- esta variable se corresponde con el dataframe del
    ejercicio 1.2.

    Parámetros de salida:
    - df_eje33 (pandas df) -- esta variable se corresponde con el dataframe que
    contiene las columnas: "name", "original_name", "networks" y "production_
    companies".
    """

    # inicializamos el dataframe donde meteremos los datos
    df_eje33 = pd.DataFrame(columns=["name", "original_name", "networks",
                                     "production_companies"])

    i = 0 # los índices para el dataframe
    for _, row in df_eje1.iterrows():
        flag = 0 # para saber si ya hemos añadido el mismo dataframe
        lang = row['languages']
        or_lang = row['original_language']
        lang_check = isinstance(lang, str) # comprobamos tipo variable

        if or_lang == 'ja':
            nombre = row['name']
            nombre_orig = row['original_name']
            networks = row['networks']
            empresas = row['production_companies']

            # ahora los añadimos al dataframe nuevo
            df_eje33.loc[i] = [nombre, nombre_orig, networks, empresas]
            flag = 1
            i += 1

        if flag == 0 and lang_check and 'ja' in lang: # lang_check es un bool
            nombre = row['name']
            nombre_orig = row['original_name']
            networks = row['networks']
            empresas = row['production_companies']

            # ahora los añadimos al dataframe nuevo
            df_eje33.loc[i] = [nombre, nombre_orig, networks, empresas]
            i += 1

    return df_eje33
