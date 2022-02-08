# Libreria Numpy

![image](https://user-images.githubusercontent.com/98423341/151892484-27eeb63f-8b33-4167-bfbc-dc39b27e81e0.png)

[Numpy](https://numpy.org/) es una libreria de python que nos proporcionara un objeto matriz multidimensional. Numpy apoya las operaciones de matrices, tales como manupulación matemática, lógica, clasificación, selección, transformadas discretas, algebra lineal basica, operaciones estadisticas y mucho más. [numpy](https://numpy.org/doc/stable/)


Numpy crea objetos de tipo **array** el array, lo cual es una estructura que tiene dentro de si datos numericos del mismo tipo, estos arrays pueden ser de una dos o tres dimensiones.

![image](https://user-images.githubusercontent.com/98423341/151892802-b1604137-cfac-4e91-988a-6502033d656c.png) [aprendeconalf.es](https://aprendeconalf.es/docencia/python/manual/numpy/#la-clase-de-objetos-array).

Para declara crear un array haremos los siguiente:

```python
import numpy as np # muy imoportante que cada que corras una linea de codigo de esta sección este importada Numpy
```
generalmente importamos a numpy como np para no escribir numpy cada que queramos usar la libreria. Una vez teniendo a numpy podemos crear un array desde una lista de datos tipo numerico o directamente escribiendo el array.

```python

Mi_array = [1,2,3,4,5]
Mi_array = np.array(Mi_array) # en la misma lista se creara el objeto array con los mismos valores de la lsita 
print(Mi_array)
```
O de la siguiente manera 

```python
Mi_array = np.array([1,2,3,4,5])
print(Mi_array)
```
El acceso a algún elemento de nuestro array se hara de la misma manera que en una lista:

```python
print(Mi_array[:-2])
```
Pero se dijo que Numpy nos da la posibilidad de crear matrices de hasta 3 dimensiones, para crear una matriz de 2 dimensiones o 3 dimensiones es bastante sencillo:

```python
Mi_array2D = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(Mi_array2D)
print("\n") #Esta linea nos permite separar los array, para leerlos de mejor manera
Mi_array3D = np.array ([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(Mi_array3D)
```

Si bien ahora nosotros queremos accesar a algún elemento de un array 3D o 2D lo haremos de la siguiente manera:

```python
print(Mi_array2D[1,0]) #Acceso al primer dato de la primera fila [fila, dato de la fila ]
# o de la siguiente manera
print(Mi_array2D[1][0]) 
# si queremos una fila entera
print(Mi_array2D[1]) #Acceso a la fila 1
```

Si bien quisieramos 3 primeros datos de ambas filas

```python
print(Mi_array2D[:, :3]) 
```

Con un array de tres dimensiones es mas o menos lo mismo, si buscamos al tercer valor(que seria el 3) de la primera fila, de la primera matriz:

```python
print(Mi_array3D[0,0,2]) # array3D[matriz,fila de esa matriz,posición del valor que se busca de esa fila]
```
Posteriormente veremos funciones que nos seran de mucha ayuda para nuestro curso.
