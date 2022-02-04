# LISTAS
Una lista es una coleccion de elementos de un tipo mas tipos de datos ya sean, valores enteros, flotantes, caracteres, cadenas de caracteres, etc. Estos elementos estan
almacenados en ubicaciones de memoria contiguas, como podemos ver acontinuación:

![image](https://user-images.githubusercontent.com/98423341/151888052-0e2d448b-5a9f-4713-8139-01cbf46001f6.png)
[geeksforgeeks.org](https://www.geeksforgeeks.org/python-arrays/)

Cabe resaltar que en **Python** las posiciones de llas listas empiezan desde la posición 0 y no desde 1, cómo en algunos otros lenguajes de programación

Ahora, supongamos que tenemos 10 valores de numeros enteros, del 1 al 10 y queremos guardarlos en una lista, guardaremos al valor 1 en la primera casilla de nuestra lista,
osea en la posición cero, el valor dos en la posición 1 y así sucesivamente con  los demas valores, entonces nuestros valores estarian en una posición
para cada uno de ellos y se verian de la siguiente forma:

![array](https://user-images.githubusercontent.com/98423341/151889059-e097ad95-0fdf-4076-8ebf-1992444bf892.png)

Por lo cual si nos hicieramos la pregunta, ¿Que valor hay en la posición numero 8 de nuestro lista de numeros enteros, pues la respues seria 9.

También si nosotros escribieramos un nombre como: **MARGUERITE** podriamos ver al nombre como una lista de 10 caracteres los cuales estarian acomodados de la siguiente posición.

![Lista](https://user-images.githubusercontent.com/98423341/151891768-e0f5643b-a131-4a4d-abe7-18c3f252a368.png)

Entonces cada letra o caracter estara almacenado en una posición de la lista, teniendo así un facil manejo de cada letra del nombre.

## Escritura y manejo de listas 

En Python es muy sencillo crear una lista, como ejemplo crearemos la lista de valores enteros que se vio como ejemplo, la lista se crea de la siguiente manera:

```python
Mi_lista = [1,2,3,4,5,6,7,8,9,10]
print(Mi_lista)
```
Y si nosotros queremos saber si en efecto lo que escribimos es una lista usaremos la función **type(tu lista)**
```python
Mi_lista = [1,2,3,4,5,6,7,8,9,10]
type(Mi_lista)
```
Ademas si también queremos saber de que tamaño quedo la lista que hemos creado tendremos las función **len(tu lista)**
```python
Mi_lista = [1,2,3,4,5,6,7,8,9,10]
len(Mi_lista)
```
Si nosotros quisieramos hacer la lista de caracteres de **MARGUERITE** hay dos formas de conseguirlo
```python
Nombre = ['M','A','R','G','U','E','R','I','T','E']
print(Nombre)
``` 
o de la siguiente manera

```python
Nombre = "MARGUERITE"
print(Nombre)
``` 
¿Qué pasa si nosotros solo quisieramos el dato que hay en la posición 8, cómo entramos a esa dirección y leemos el dato, o lo guardamos?. De la siguiente manera

```python
Mi_lista = [1,2,3,4,5,6,7,8,9,10] # creamos nuestra lista
#Si solo queremos leer un valor haremos lo siguiente
print(Mi_lista[8])# Nos mostrara el valor que hay en la posición 8 de nuestra lista
#Si queremos guardar un valor, para despues usarlo o simplemente visualisarlo
Pos_ocho = Mi_lista[8]
print(Pos_ocho)
``` 
De esta manera podemos obtener los datos que hay en cierta posición especifica de nuestra lista
