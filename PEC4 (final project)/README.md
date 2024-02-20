
# PEC4

Este proyecto se corresponde con la última PEC de la asignatura. En esta PEC se nos dan 3 datasets, a partir de los cuales se han desarrollado funciones con código Python que dan respuesta a las preguntas enunciadas en el archivo `ES-PEC4-PabloSuarezReyero-SOLUCION.ipynb`. En este último, uno puede encontrar explicaciones adicionales acerca de cada una de las implementaciones asociadas a cada uno de los ejercicios.

## Organización

La organización de esta PEC, es la que ya se conoce del enunciado. Es por esto, que este apartado se centra en explicar el contenido del `.zip` relacionando los archivos planos `.py` desarrollados con cada uno de los ejercicios vistos en el enunciado.

El arhivo `.zip` donde se encuentra este archivo, contiene los siguientes ficheros:

- **data/**: Esta es una carpeta que contiene los 3 csv's, y el zip original que los contenía.

- **results/**: Esta carpeta contiene los *dataframes* que se pide crear en los ejercicios 1.2 y 2.1, y los tres gráficos que se piden en los ejercicios 4.1, 4.2, 4.3.

- **tests/**: Esta carpeta contiene el código: `test_codes` que permite verificar el correcto funcionamiento del código desarrollado en esta PEC. Además también se encontraran los informes en formato `HTML` para verificar que los códigos que se han desarrollado han "aprobado".

- `ES-PEC4-PabloSuarezReyero-SOLUCION.ipynb`: Este archivo de extensión `.ipynb` contiene el enunciado de la PEC con las explicaciones, aclaraciones y referencias de cada uno de los ejercicios. Además, en este mismo archivo están las soluciones a los ejercicios que no requieren de código para su solución, i.e., los ejercicios: 1.4, aquellos que requieran explicar los resultados, y el ejercicio 5.

- `requirements.txt`: Este archivo contiene las librerías requeridas para poder correr los códigos sin problema.

- `analisis_grafico.py`: Este archivo plano `.py`, contiene el código correspondiente a toda la resolución del ejercicio 4, i.e., 4.1, 4.2, 4.3.

- `descomp_lectura.py`: Este archivo plano `.py`, contiene el código correspondiente a toda la resolución del ejercicio 1, i.e., 1,1, 1.2 y 1.3. Nótese como el ejercicio 1.4, al ser una respuesta escrita, se encuentra resuelto en el enunciado de esta PEC 4, en el archivo `ES-PEC4-PabloSuarezReyero-SOLUCION.ipynb`. Para aclaraciones, explicaciones o referencias usadadas para el desarrollo del código, acudir al ejercicio 1, en el mismo archivo `ES-PEC4-PabloSuarezReyero-SOLUCION.ipynb`

- `filtrado_datos.py`: Este archivo plano `.py`, contiene el código correspondiente a toda la resolución del ejercicio 3, i.e., 3,1, 3.2 y 3.3. Para aclaraciones, explicaciones o referencias usadadas para el desarrollo del código, acudir al ejercicio 3, en el archivo `ES-PEC4-PabloSuarezReyero-SOLUCION.ipynb`

- `procesado_datos.py`: Este archivo plano `.py`, contiene el código correspondiente a toda la resolución del ejercicio 2, i.e., 2,1 y 2.2. Para aclaraciones, explicaciones o referencias usadadas para el desarrollo del código, acudir al ejercicio 2, en el archivo `ES-PEC4-PabloSuarezReyero-SOLUCION.ipynb`

- `testing_imports.py`: Este archivo plano `.py`, se encarga de importar todas las funciones desarrolladas, para utilizarlas en el archivo de `tests.py`

- `main.py`: Este archivo plano `.py`, es desde donde se llama al resto de funciones desarrolladas en todos los archivos planos mencionados antes.

- **/htmlcov**: Esta fichero contiene los resultados de cobertura de los tests.

- **/informes**: Esta carpeta contiene los resultados de los test de la PEC.


## Como lanzar la ejecución del código

Para poder correr el código primero hay que situarnos en la carpeta descomprimida y abrir una terminal. Para recrear mi entorno de trabajo, a continuamos procdemos a crear un entorno con anaconda.

```
conda create -n myenv python=3.10.13
```
Ahora se activa el entorno virtual:

```
conda activate myenv
```
Se ha creado un entorno con anaconda, porque era la única opción que me funcionaba, ya que no puedo instalar la máquina virtual debido a la arquitectura de procesador que tengo. Además, a la hora de crear un `virtualenv`, se me añadían muchísimos paquetes de python en el documento de `requirements.txt` que luego a la hora de instalarlos me generaban problemas.

En principio, no debería de hacer falta crear un entorno virtual, pero este es interesante de cara al manejo de librerias, sobretodo cuando uno tiene varias asignaturas o proyectos donde usa diferentes librerías.

Habiendo seguido las pautas de la creación de un entorno virtual con anaconda, una vez ya se ha activado el entorno virtual, ya estamos en condiciones de instalar las librerías con las versiones exactas, para ello, introduciremos el siguiente comando en nuestra terminal:

```
pip install -r requirements.txt
```
Según se terminen de instalar las librerías enunciadas en el archivo `requirements.txt`, ya podemos ejecutar el fichero "nodriza", i.e., el fichero `main.py`. Para ello, si se quieren ejecutar todas las funciones de manera secuencial, introduciremos el siguiente comando:

```
python main.py
```
Hace falta notar que con `python3` no funciona, el comando tiene que ser con `python`.

En el caso de esta PEC, al haber dependencias de datos entre ejercicios, para poder ejecutar las funciones de los ejercicios 2, 3 o 4, se ha de ejecutar primero el ejercicio 1 (siempre). No obstante, si uno solo quiere ejecutar el primer ejercicio puede hacerlo sin problema.

En el caso de querer ejecutar el segundo ejercicio, tendrá que ejecutarse el primer ejercicio, porque el segundo ejercicio depende de los datos producidos en el primero. Aunque, cabe destacar, que entre el ejercicio 3 y 4 no hay dependencias, por lo tanto, para poder ejecutar el ejercicio 4, solamente habrá que ejecutar los ejercicios: 1,2 y 4.

El programador también tiene la libertad de ejecutar todas las funciones especificando el argumento "todos" al final de la expresión `python main.py` o simplemente dejándola tal cual.

Los argumentos que el programa acepta son:
- Parar ejecutar todo -> `python main.py`.
- Para ejecutar el primer ejercicio -> `python main.py 1`.
- Para ejecutar el segundo ejercicio -> `python main.py 2`. En este caso también se ejecuta el primer ejercicio.
- Para ejecutar el tercer ejercicio -> `python main.py 3`. En este caso también se ejecutan tanto el primer como segundo ejercicio.
- Para ejecutar el cuarto ejercicio -> `python main.py 4`. En este caso también se ejecutan tanto el primero como el segundo ejercicio.


## Comprobación, tests y cobertura

En este apartado se explica con detalle como lanzar las simulaciones de los tests y como calcular la cobertura de los mismos.

Para comprobar el correcto funcionamiento de los códigos, se ha implementado el código `test_codes.py`. Este código permite comprobar los aspectos fundamentales de cada una de las funciones que se han creado.

Para correr los tests y ejecutarlos hay que escribir el siguiente comando en el terminal:

```
python -m tests.test_codes
```
Tras la ejecución de los `tests` ya podemos conocer la cobertura de los tests. Para ello, en el mismo directorio desde el cual hemos ejecutado tanto el `main.py` como `tests.test_code.py`, ejecutaremos el siguiente comando:

```
coverage run -m unittest discover
```

Ya se ha claculado la cobertura, ahora hay que visualizarla, para ello ejecutamos el siguiente comando:

```
coverage report -m
```
Este comando nos mostrará en nuestra consola el resultado del número de *statements*, de *misses* y la cobertura calculada para cada función. Finalmente, la cobertura total del proyecto, se muestra al final de la ejecución en la consola.  

Adicionalmente, también tenemos a nuestra disposición una visualización de más alto nivel, en la que podremos revisar función a función, cada una de las lineas de código que han fallado. Los archivos generados por el siguiente comando, tienen un formato `HTML`.

```
coverage html
```

## Problemas con `virtualenv`

Como se ha comentado antes, a la hora de crear un entorno virtual con la librería de python `virtualenv`, a la hora de actualizar el fichero de `requirements.txt` se añadían muchas librerías innecesarias, que luego daban problemas a la hora de instalarlas. Estas librerías se han recopilado aquí:

```
attr==0.3.2
ConfigParser==6.0.0
contextlib2==21.6.0
cryptography==41.0.3
Cython==3.0.8
dl==0.1.0
docutils==0.20.1
filelock==3.13.1
HTMLParser==0.0.2
ipython==8.15.0
ipywidgets==8.1.1
Jinja2==3.1.2
jnius==1.1.0
keyring==24.3.0
matplotlib==3.8.2
mock==5.1.0
pandas==2.2.0
Pillow==10.1.0
Pillow==10.2.0
protobuf==4.25.2
pyOpenSSL==23.2.0
pyOpenSSL==23.3.0
railroad==0.5.0
redis==5.0.1
Sphinx==7.2.6
thread==0.1.3
tornado==6.3.3
trove_classifiers==2024.1.8
urllib3_secure_extra==0.1.0
xmlrpclib==1.0.1
```
No obstante, a la hora de trabajar con un entorno de anaconda, las únicas librerías que se han de instalar son las que se encuentran en el archivo `requirements.txt`, que son:

```
coverage==7.4.0
html_testRunner==1.2.1
HTMLTestRunner==0.8.0
HtmlTestRunner==0.8.0
HTMLTestRunner_rv==1.1.2
matplotlib==3.8.2
pandas==2.2.0
```





