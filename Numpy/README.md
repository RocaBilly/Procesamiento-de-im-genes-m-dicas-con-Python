# Libreria Numpy

![image](https://user-images.githubusercontent.com/98423341/151892484-27eeb63f-8b33-4167-bfbc-dc39b27e81e0.png)

[Numpy](https://numpy.org/) es una libreria de python que nos proporcionara un objeto matriz multidimensional. Numpy apoya las operaciones de matrices, tales como manupulación matemática, lógica, clasificación, selección, transformadas discretas, algebra lineal basica, operaciones estadisticas y mucho más. [numpy](https://numpy.org/doc/stable/)


Numpy crea objetos de tipo **array** el array, lo cual es una estructura que tiene dentro de si datos numericos del mismo tipo, estos arrays pueden ser de una dos o tres dimensiones.

![image](https://user-images.githubusercontent.com/98423341/151892802-b1604137-cfac-4e91-988a-6502033d656c.png) [aprendeconalf.es](https://aprendeconalf.es/docencia/python/manual/numpy/#la-clase-de-objetos-array).

Para declara crear un array haremos los siguiente:

```python
import numpy as np
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
