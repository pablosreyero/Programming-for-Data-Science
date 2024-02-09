"""
En este archivo se encuentran las funciones relativas al ejercicio nº4.
"""

import re
import pandas as pd
import matplotlib.pyplot as plt


def grafico_barras(df_air_days):
    """
    Esta función se encarga de representar en una gráfico de barras, el número
    de series por año de inicio.

    Parámetros de entrada:
    - df_air_days (pandas df) -- esta variable se corresponde con el dataframe
    del ejercicio 2.1.

    Nótese como esta función no retorna ninguna variable.
    """
    # tal y como se explica en la aclaración que puede verse en el enunciado
    # del jupyter notebook del ejercicio 4.1, primero vamos a limpiar el df

    # primero hacemos una copia del df
    df_eje2_1 = df_air_days.copy(deep = True)
    regex_list = [r'^1917', r'^1921', r'^2024', r'^2025', r'^2026', r'^2029']
    for index, row in df_eje2_1.iterrows():
        fecha = row['first_air_date']
        fecha_check = isinstance(fecha, str) # comprobamos tipo variable
        if fecha_check:
            for regex_i in regex_list:
                check_er = bool(re.match(regex_i, fecha))
                if check_er:
                    df_eje2_1 = df_eje2_1.drop(index = index)

    # Convertimos la columna de 'first_air_date' a tipo datetime
    df_eje2_1['first_air_date'] = pd.to_datetime(df_eje2_1['first_air_date'])
    # extraemos el año de la columna 'first_air_date' creando una col nueva
    df_eje2_1['anio'] = df_eje2_1['first_air_date'].dt.year
    # contamos el número de series por año
    series_por_anio = df_eje2_1['anio'].value_counts().sort_index()
    # creamos la gráficade barras
    series_por_anio.plot.bar()

    # representamos
    plt.ylabel('Número de series')
    plt.xlabel('Año de emisión')
    plt.title('Número de series por año de emisión')

    # ahora guardamos la figura
    plt.savefig("results/numero_series_anio.jpg")

    plt.show()


def grafico_lineas(df_air_days):
    """
    En esta función se construye un gráfico de lineas que muestra el número de
    series de cada categoría de la variable “type” producidas en cada década
    desde 1940.

    Parámetros de entrada:
    - df_air_days (pandas df) -- esta variable se corresponde con el dataframe
    del ejercicio 2.1.

    Nótese como esta función no retorna ninguna variable ni ningún valor.
    """

    # creamos un dataframe nuevo para tener solo las dos cols que nos interesan
    df_eje42 = pd.DataFrame(columns=["decadas", "tipos"])

    # recorremos el dataset original, para extraer info y meterla en df_eje42
    i = 0
    for _, row in df_air_days.iterrows():
        fecha = row['first_air_date']
        fecha_check = isinstance(fecha, str) # comprobamos tipo variable
        if fecha_check:
            anio = int(fecha[0:4])
            if anio >= 1940:
                decada = (anio // 10) * 10
                tipo = row["type"]
                df_eje42.loc[i] = [decada, tipo]
                i += 1

    # ahora montamos la gráfica
    cuenta = df_eje42.groupby(['decadas', 'tipos']).size().unstack().fillna(0)

    # Crear un gráfico de líneas para cada categoría de 'type'
    cuenta.plot(kind = 'line')

    # Configurar el gráfico
    plt.ylabel('Número de series')
    plt.xlabel('Década')
    plt.title('Número de series por década y tipo')
    plt.legend(title = 'Tipo')

    # ahora guardamos la figura
    plt.savefig("results/numero_series_decada.jpg")
    plt.show()



def grafico_circular(df_eje1):
    """
    Esta función se encarga de crear un gráfico circular donde se muestra el %
    de tipo de series, dependiendo de su género. Aquellas géneros que represen-
    ten menos del 1% del total, serán incluidas en el apartado 'Other'.

    Parámetros de entrada:
    -df_eje1 (pandas df) -- esta variable se corresponde con el dataframe del
    ejercicio 1.2.

    Parámetros de salida:
    -nseries_por_gen () -- esta variable contiene el nº de series por género.
    """

    # hacemos una copia del df original.
    df_43 = df_eje1.copy(deep = True)

    # obviamos celdas vacías y especificamos la separación entre multigenero
    df_43 = df_43[df_43['genres'].notna()]
    df_43['genres'] = df_43['genres'].str.split(', ')

    # calculamos los porcentajes
    generos_todos = [genero for lst_gen in df_43['genres']
                     for genero in lst_gen]
    #print(generos)

    nseries_por_gen = pd.Series(generos_todos).value_counts()
    cuenta_generos_n = pd.Series(generos_todos).value_counts(normalize=True)
    # print(cuenta_generos_n)

    # si genero representa < 1% entonces lo metemos en "others"
    generos_filt = cuenta_generos_n[cuenta_generos_n >= 0.01].index
    # print('\n \n', generos_filt)
    df_43['filtered_genres'] = df_43['genres'].apply(
        lambda generos:[genero if genero in generos_filt else 'others'
                        for genero in generos])

    cuenta_gen_filt = pd.Series([genero
                                 for lst_gen
                                 in df_43['filtered_genres']
                                 for genero
                                 in lst_gen]).value_counts(normalize=True)

    # creamos el gráfico 'PIE CHART'
    plt.pie(cuenta_gen_filt, labels=cuenta_gen_filt.index, autopct='%1.1f%%')
    plt.title('Distribución de Géneros')

    # ahora guardamos la figura
    plt.savefig("results/generos_porcent_piechart.jpg")
    plt.show()

    return nseries_por_gen
