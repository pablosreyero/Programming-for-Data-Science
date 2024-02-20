"""
En este archivo se encuentra el main, y dentro de él las llamadas al resto de
funciones desarrolladas en archivos .py planos
"""

import sys

# Ahora importamos los ficheros con las funciones
import descomp_lectura
import procesado_datos
import filtrado_datos
import analisis_grafico


def process_arguments(args, ejercicios):
    """
    Procesa los argumentos que determinan que ejercicio(s) ha(n) de ejecutarse
    """

    if len(args) > 2:
        sys.exit('ERROR: demasiados argumentos')

    elif len(args) == 2:
        ejercicio = int(args[1])
        if ejercicio < 1 or ejercicio > len(ejercicios)-1:
            sys.exit('ERROR: argumento inválido')

        else:
            return ejercicio

    else:
        return 'todos'


def ejecucion_ejercicio1():
    """
    Esta función ejecuta las funciones del primer ejercicio de la PEC. 
    Recibe como parámetro de entrada, la ruta del fichero que
    tiene que descomprimir:
    - ruta_archivo (str) -- la ruta del archivo .zip.

    Parámetro de salida:
    - df_eje1 (pandas df) -- el dataframe creado en el ejercicio, necesario
    para el resto de ejercicios.
    """

    # Definimos la ruta donde está el .zip
    ruta_archivo = "data/TMDB.zip"

    # Ejercicio 1.1
    print('Ejercicio 1.1\n')
    booleano = descomp_lectura.descompresion(ruta_archivo)
    print(booleano)
    # la variable que devuelve arriba escpara luego hacer el testing

    # Ejercicio 1.2
    print('\nEjercicio 1.2\n')
    df_eje1, t_pandas = descomp_lectura.lectura_pandas(ruta_archivo)
    print(f'El tiempo transcurrido es de {t_pandas} segundos')
    print('Este es el número de cols: ', len(df_eje1.columns))

    # ahora guardamos el csv para comprobar
    df_eje1.to_csv('results/df_eje1.csv')

    # Ejercicio 1.3
    print('\nEjercicio 1.3\n')
    dict_final, t_csvs = descomp_lectura.lectura_csvs(ruta_archivo)
    print(f'\nEl tiempo transcurrido es de {t_csvs} segundos')
    print(f'El tamaño del diccionario es el siguiente: {len(dict_final)}')
    ultimos_2 = {k: dict_final[k] for k in list(dict_final)[162136:162138]}
    print(f'\nLos 2 últimos dicts anidados: {ultimos_2}\n')
    print(len(ultimos_2['240424']))

    return df_eje1


def ejecucion_ejercicio2(df_eje1):
    """
    Esta función ejecuta las funciones del segundo ejercicio de la PEC. 
    Recibe como parámetro de entrada, el df creado en el ejercicio anterior:
    - df_eje1 (pandas df) -- dataframe del ejercicio 1.2.

    Parámetros de salida:
    - df_air_days (pandas df) -- dataframe creado en el ejercicio, que se
    usará en otros ejercicios.
    """

    # Ejercicio 2.1
    print('Ejercicio 2.1\n')
    df_air_days, df_final = procesado_datos.df_nueva_variable(df_eje1)
    print(df_final.head(10), "\n")

    # ahora guardamos el csv para comprobar
    df_final.to_csv('results/df_final.csv')
    df_air_days.to_csv('results/df_air_days.csv')

    # Ejercicio 2.2
    print('Ejercicio 2.2\n')
    dict_22 = procesado_datos.diccionario2_2(df_eje1)

    # ahora mostramos los 5 primeros elementos del diccionario
    dict_22_5 = dict(list(dict_22.items())[:5])
    print(f'Aquí las 5 primeras entradas del diccionario:\n {dict_22_5}\n')

    return df_air_days


def ejecucion_ejercicio3(df_eje1, df_air_days):
    """
    Esta función ejecuta las funciones del segundo ejercicio de la PEC.

    Parámetros de entrada:
    - df_eje1 (pandas df) -- El df creado en el ejercicio 1.2.
    - df_air_days (pandas df) -- El df creado en el ejercicio 2.1. 
    """

    # Ejercicio 3.1
    print('Ejercicio 3.1\n')
    lista_series31 = filtrado_datos.series_31(df_eje1)
    print(f'Esta es la lista de las series: \n{lista_series31}\n')

    # Ejercicio 3.2
    print('Ejercicio 3.2\n')
    lista_series32 = filtrado_datos.series_32(df_air_days)
    print(f'Esta es la lista de las series: \n{lista_series32[:20]}\n')

    # Ejercicio 3.3
    print('Ejercicio 3.3\n')
    df_eje33 = filtrado_datos.dataframe_33(df_eje1)
    print(df_eje33.head(20), "\n")


def ejecucion_ejercicio4(df_eje1, df_air_days):
    """
    Esta función ejecuta las funciones del segundo ejercicio de la PEC.

    Parámetros de entrada:
    - df_eje1 (pandas df) -- El df creado en el ejercicio 1.2.
    - df_air_days (pandas df) -- El df creado en el ejercicio 2.1. 
    """

    # Ejercicio 4.1
    print('Ejercicio 4.1\n')
    analisis_grafico.grafico_barras(df_air_days)

    # Ejercicio 4.2
    print('Ejercicio 4.2\n')
    analisis_grafico.grafico_lineas(df_air_days)

    # Ejercicio 4.3
    print('Ejercicio 4.3\n')
    n_series_por_gen = analisis_grafico.grafico_circular(df_eje1)
    print(f'\nEl nº de series por género es: \n\n{n_series_por_gen}')


# definimos la función principal
def main(args):
    """
    Esta función alberga todas las llamadas al resto de funciones
    desarrolladas en este proyecto. Esta función ni recibe ni 
    expide ningún parámetro.
    """

    ejercicios = [None, ejecucion_ejercicio1, ejecucion_ejercicio2,
                  ejecucion_ejercicio3, ejecucion_ejercicio4]

    # Ahora comprobamos si los argumentos son correctos
    ejercicio = process_arguments(args, ejercicios)
    # Ejecutamos el ejercicio elegido
    if ejercicio == 'todos':
        # Ejecución ejercicio 1
        df_eje1 = ejecucion_ejercicio1()
        # Ejecución ejercicio 2
        df_air_days = ejecucion_ejercicio2(df_eje1)
        # Ejecución ejercicio 3
        ejecucion_ejercicio3(df_eje1, df_air_days)
        # Ejecución ejercicio 4
        ejecucion_ejercicio4(df_eje1, df_air_days)

    elif ejercicio == 1:
        # Ejecución ejercicio 1
        df_eje1 = ejecucion_ejercicio1()

    elif ejercicio == 2:
        # Ejecución ejercicio 1
        df_eje1 = ejecucion_ejercicio1()
        # Ejecución ejercicio 2
        df_air_days = ejecucion_ejercicio2(df_eje1)

    elif ejercicio == 3:
        # Ejecución ejercicio 1
        df_eje1 = ejecucion_ejercicio1()
        # Ejecución ejercicio 2
        df_air_days = ejecucion_ejercicio2(df_eje1)
        # Ejecución ejercicio 3
        ejecucion_ejercicio3(df_eje1, df_air_days)

    elif ejercicio == 4:
        # Ejecución ejercicio 1
        df_eje1 = ejecucion_ejercicio1()
        # Ejecución ejercicio 2
        df_air_days = ejecucion_ejercicio2(df_eje1)
        # Ejecución ejercicio 4
        ejecucion_ejercicio4(df_eje1, df_air_days)


# llamamos al main
if __name__ == "__main__":
    main(sys.argv)
