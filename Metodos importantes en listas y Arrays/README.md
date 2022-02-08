# Funciones en Arrays y listas 

A continuación veremos algunas funciones de las listas o arrays que nos serviran a lo largo del curso.

## Arrays

```python

import numpy as np

# np.empty(dimensiones) Crea y devuelve una referencia a un array vacío con las dimensiones especificadas en la tupla dimensiones.

empty = np.empty((2,2))

#np.linspace(inicio, fin, n)Crea un array de una dimensión cuyos elementos son la secuencia de n valores equidistantes desde inicio hasta fin.


space = np.linspace(1,100,10)

print(space)

#np.arange(inicio, fin, salto) : Crea un array de una dimensión cuyos elementos son la secuencia desde inicio hasta fin tomando valores cada salto.
#muy parecido a linspace, el fin es abierto

ara = np.arange (0,100,10)
print(ara)

#np.full(dimensiones, valor) : Crea un array con las dimensiones especificadas rellenandola de el valor.

valor = np.full((2,3),12)
print(valor)

#np.random.rand*dimensiones) Crea un array con dimensón dada cuyos elementos son aleatorios.  
ran = np.random.rand(2,3)
print (ran)

#ademas tenemos unos atributos de los arrays que creamos
 

#array.shape : Devuelve una tupla con las dimensiones del array.

#array.size : Devuelve el número de elementos del array.

#array.dtype: Devuelve el tipo de datos de los elementos del array.

ara = np.arange (0,100,10)


print(ara.shape)
print(ara.size)
print(ara.dtype)


```

*rnd es el tipo de distibución de los valores, este puede variar, 
para conocer estas distribuciones visite la siguiente pagina [numpy random](https://numpy.org/doc/stable/reference/random/generated/numpy.random.rand.html)

## Listas 

```python

#Lista.append agrega un valor a la lista en la ultima posición cada que se usa ya sea una lista vacia o una que ya tenga valores.

Lista= []
Lista.append(1)
Lista.append(2)
Lista.append(3)
print(Lista)

Datos =[1,2,3,'A']
Datos.append('B')
Datos.append('C')
print(Datos)

#Si bien no quieres que los valores se vayan agregando al final de la lista y quieres agregalo en una posición especifica usaremos el metodo .insert
Datos =[1,2,3,'A']
Datos.insert(1,5)
print(Datos)

#Obsevemos que agregara el numero 5 en la posición 1 y el 2 que estaba en la posición 1 lo movera a la posición 2


# Si nosotros queremos eliminar un dato de nuestra lista y que ya no este ni el dato ni su espacio que ocupaba usaremos el metodo .remove("dato que queremos eliminar")
Datos =[1,2,3,'A']
Datos.remove('A') #Debemos saber bien que tipo es el dato que eliminaremos 
print(Datos)

#Si queremos saber cuantas veces se repite un elemento de nuestro interes en la lista, usaremos el métod .count(valor)
repe = [1,1,1,1,1,3,4,5]
cont = repe.count(1)
print(f'El 1 se repite {cont} veces')

```
