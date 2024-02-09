'''
Este archivo contiene los códigos de los test para nuestro proyecto
'''

import unittest
from testing_imports import *
from HtmlTestRunner import HTMLTestRunner
# from HTMLTestRunner import HTMLTestRunner
import coverage


class Test_descomp_lectura(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.ruta_archivo = "data/TMDB.zip"
        cls.df_1 = pd.read_csv("data/TMDB_distribution.csv")
        cls.df_2 = pd.read_csv("data/TMDB_info.csv")
        cls.df_3 = pd.read_csv("data/TMDB_overview.csv")

    def test_decompresion(self):
        """
        Comprobación del funcionamiento de 'descompresion'
        """
        # comprobamos que la ruta es un string
        self.assertIsInstance(self.ruta_archivo, str)
        booleano = descompresion(self.ruta_archivo)
        # comprobamos que el archivo se ha descomprimido correctamente
        self.assertEqual(booleano, True)

    def test_lectura_pandas(self):
        """
        Comprobación del funcionamiento de 'lectura_pandas'
        """
        # comprobamos que la ruta que se pasa es un 'str'
        self.assertEqual(isinstance(self.ruta_archivo, str), True)
        df_eje1, t_pandas = lectura_pandas(self.ruta_archivo)
        # comprobmoas que el tiempo es 'float'
        self.assertIsInstance(t_pandas, float)
        # comprobamos que se ha generado un df de pandas
        self.assertIsInstance(df_eje1, pd.DataFrame)
        # comprobamos que el nº de columnas es 29
        self.assertEqual(len(df_eje1.columns), 29)
        # comprobamos el nº de registros es igual que el archivo original
        self.assertEqual(len(df_eje1), 162138)
        # comprobamos que el tiempo es positivo
        self.assertEqual(t_pandas > 0, True)
        # comprobamos que el df tiene el mismo nº de regs respeecto a los origs
        self.assertEqual(len(df_eje1), len(self.df_1))
        self.assertEqual(len(df_eje1), len(self.df_2))
        self.assertEqual(len(df_eje1), len(self.df_3))
        # comprobamos el nº de columnas
        self.assertEqual(len(df_eje1.columns),
                         len(self.df_1.columns)+
                         len(self.df_2.columns)+
                         len(self.df_3.columns)-2)
        print('LLego aquí')

    def test_lectura_csvs(self):
        """
        Comprobación del funcionamiento de 'lectura_csvs'
        """
        # comprobamos que la ruta que se pasa es un 'str'
        self.assertEqual(isinstance(self.ruta_archivo, str), True)
        dict_final, t_csvs = lectura_csvs(self.ruta_archivo)
        # comprobamos que el tiempo es positivo
        self.assertEqual(t_csvs > 0, True)
        # comprobamos que se trata de un diccionario
        self.assertIsInstance(dict_final, dict)
        # comprobamos que el nº de filas con el tamaño del diccionario creado
        self.assertEqual(len(dict_final), len(self.df_1))
        self.assertEqual(len(dict_final), len(self.df_2))
        self.assertEqual(len(dict_final), len(self.df_3))
        self.assertEqual(len(dict_final["240438"]), len(dict_final['240424']))
        # comprobamos el nº de columnas
        self.assertEqual(len(dict_final["240438"]), 29-1)
        self.assertEqual(len(dict_final["240424"]), 29-1)
        self.assertEqual(len(dict_final["240438"]),
                         len(self.df_1.columns)+
                         len(self.df_2.columns)+
                         len(self.df_3.columns)-3)


class Test_procesado_datos(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.ruta_df_eje1 = "results/df_eje1.csv"
        cls.df_eje1 = pd.read_csv(cls.ruta_df_eje1)

    def test_df_nueva_variable(self):
        """
        Comprobación del funcionamiento de 'df_nueva_variable'
        """
        # comprobamos que introducimos un dataframe
        self.assertIsInstance(self.df_eje1, pd.DataFrame)
        df_air_days, df_final = df_nueva_variable(self.df_eje1)
        self.assertIsInstance(df_air_days, pd.DataFrame)
        self.assertIsInstance(df_final, pd.DataFrame)
        # comprobamos que tienen el mismo nº de filas
        self.assertEqual(len(df_air_days), len(df_final))
        self.assertEqual(len(df_air_days), len(self.df_eje1))
        self.assertEqual(len(df_final), len(self.df_eje1))
        # comprobamos que tienen el mismo nº de columnas
        self.assertEqual(len(df_air_days.columns), len(df_final.columns))
        self.assertEqual(len(df_air_days.columns), len(self.df_eje1.columns))
        self.assertEqual(len(df_final.columns), len(self.df_eje1.columns))
        # comprobamos que la columna que queremos existe en el nuevo df
        self.assertEqual('air_days' in df_final.columns, True)
        self.assertEqual('air_days' in df_air_days.columns, True)
        # comprobamos que en la 1º fila del df, en 'networks', aparece la CBS
        self.assertEqual(df_final.iloc[0]['networks'], 'CBS')
        # comprobamos que el 1º valor es int (si lo es, el resto también lo es)
        # self.assertIsInstance(df_final.iloc[0]['air_days'], int)


    def test_diccionario2_2(self):
        """
        Comprobación del funcionamiento de 'diccionario2_2'
        """
        dict_22 = diccionario2_2(self.df_eje1)
        # comprobmaos que se trata de un diccionario
        self.assertIsInstance(dict_22, dict)
        # comprobamos que hay menos claves que registros, ver la explicación de
        # la implementación del ejercicio 2.2, para saber porque esto es así
        self.assertNotEqual(len(dict_22), len(self.df_eje1))
        # comprobamos que la primera clave del diccionario es 'Game of Thrones'
        self.assertEqual(str(list(dict_22.keys())[0]), 'Game of Thrones')
        # comprobamos que los strings acaban con un .jpg (el primero)
        primer_valor = list(dict_22.values())[0][0]
        self.assertEqual(primer_valor.endswith('.jpg'), True)



class Test_filtrado_datos(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.ruta_df_eje1 = "results/df_eje1.csv"
        cls.df_eje1 = pd.read_csv(cls.ruta_df_eje1)

    def test_buscar_palabras(self):
        """
        Comprobación del funcionamiento de 'buscar_palabras'
        """
        cadena1 = "Esta pelicula trata sobre un crime"
        cadena2 = "Esta pelicula trata sobre un CrIMe"
        cadena3 = "Todo esto es un mySTeRy"
        cadena4 = "Tot aixo es un mystery"
        cadena5 = 'A Majadahonda no hi ha crim'
        cadena6 = 'eN'
        cadena7 = 'en'
        cadena8 = 'EN'
        cadena9 = 'En'
        cadena10 = 'es'
        valor1 = 1
        valor2 = 2

        booleano = buscar_palabras(cadena1, valor1)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena2, valor1)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena3, valor1)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena4, valor1)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena5, valor1)
        self.assertEqual(booleano, False)
        booleano = buscar_palabras(cadena6, valor2)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena7, valor2)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena8, valor2)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena9, valor2)
        self.assertEqual(booleano, True)
        booleano = buscar_palabras(cadena10, valor2)
        self.assertEqual(booleano, False)


    def test_series_31(self):
        """
        Comprobación del funcionamiento de 'series_31'
        """
        # comprobamos que se trata de un dataframe
        self.assertIsInstance(self.df_eje1, pd.DataFrame)
        lista_series31 = series_31(self.df_eje1)
        # comprobamos que se trata de una lista
        self.assertIsInstance(lista_series31, list)
        # comprobamos que el primer elemento es un str
        self.assertIsInstance(lista_series31[0], str)
        # comprobamos que el último elemento es un str
        self.assertIsInstance(lista_series31[-1], str)
        # comprobamos que el tamaño no coincide con las filas de self.df_eje1
        self.assertNotEqual(len(lista_series31), len(self.df_eje1))


    def test_series_32(self):
        """
        Comprobación del funcionamiento de 'series_32'
        """
        # comprobamos que se trata de un dataframe
        self.assertIsInstance(self.df_eje1, pd.DataFrame)
        lista_series32 = series_32(self.df_eje1)
        # comprobamos que se trata de una lista
        self.assertIsInstance(lista_series32, list)
        # comprobamos que el primer elemento es un str
        self.assertIsInstance(lista_series32[0], str)
        # comprobamos que el último elemento es un str
        self.assertIsInstance(lista_series32[-1], str)
        # comprobamos que el tamaño no coincide con las filas de self.df_eje1
        self.assertNotEqual(len(lista_series32), len(self.df_eje1))

    def test_dataframe_33(self):
        """
        Comprobación del funcionamiento de 'dataframe_33'
        """
        # comprobamos que se trata de un dataframe
        self.assertIsInstance(self.df_eje1, pd.DataFrame)
        df_eje33 = dataframe_33(self.df_eje1)
        # comprobamos que devuelve un dataframe
        self.assertIsInstance(df_eje33, pd.DataFrame)
        # comprobamos que hay 4 columnas
        self.assertEqual(len(df_eje33.columns), 4)
        # comprobamos que no tienen el mismo nº de registros
        self.assertNotEqual(len(df_eje33), len(self.df_eje1))
        # comprobamos que no tienen el mismo nº de columnas
        self.assertNotEqual(len(df_eje33.columns), len(self.df_eje1.columns))
        # comprobamos que la columna 'name' está en el dataframe resultante
        self.assertEqual('name' in df_eje33.columns, True)
        # comprobamos que la columna 'original_name' está en el dataframe resul
        self.assertEqual('original_name' in df_eje33.columns, True)
        # comprobamos que la columna 'networks' está en el dataframe resultante
        self.assertEqual('networks' in df_eje33.columns, True)
        # comprobamos que la columna 'production_companies' está en el df resul
        self.assertEqual('production_companies' in df_eje33.columns, True)


class Test_analisis_grafico(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.ruta_df_eje1 = "results/df_eje1.csv"
        cls.df_eje1 = pd.read_csv(cls.ruta_df_eje1)
        cls.ruta_df_air_days = "results/df_air_days.csv"
        cls.df_air_days = pd.read_csv(cls.ruta_df_air_days)

    def test_grafico_barras(self):
        """
        Comprobación del funcionamiento de 'grafico_barras'
        """
        # comprobamos que introducimos un dataframe
        self.assertIsInstance(self.df_air_days, pd.DataFrame)
        grafico_barras(self.df_air_days)

    '''def test_grafico_lineas(self):
        """
        Comprobación del funcionamiento de 'grafico_lineas'
        """
        # comprobamos que introducimos un dataframe
        self.assertIsInstance(self.df_air_days, pd.DataFrame)
        grafico_lineas(self.df_air_days)'''

    def test_grafico_circular(self):
        """
        Comprobación del funcionamiento de 'grafico_circular'
        """
        # comprobamos que introducimos un dataframe
        self.assertIsInstance(self.df_eje1, pd.DataFrame)
        nseries_por_gen = grafico_circular(self.df_eje1)
        # comprobamos que nseries_por_gen es pd.Series
        self.assertIsInstance(nseries_por_gen, pd.Series)



if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Test_descomp_lectura))
    suite.addTest(unittest.makeSuite(Test_procesado_datos))
    suite.addTest(unittest.makeSuite(Test_filtrado_datos))
    suite.addTest(unittest.makeSuite(Test_analisis_grafico))
    runner = HTMLTestRunner(log=True, verbosity=2, output='informes',
                            title='PEC4', description='PEC4 tests',
                            report_name='Tests PEC4')
    
    runner.run(suite)
