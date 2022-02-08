# Ciclos y condicionales 
- ### If: 
If es una función de condición, donde si se cumple cierta condición dada por el usuario, 
se correrá una determinada línea de código, 
y si no se cumple o se podrá seguir con el programa normalmente o hacer una cosa diferente.

La condicional If tendra la siguiente estructura: 

```python
#if(condición):
  #bloque de codigo

#es importante saber que el bloque de codigo dentro del if, debe estar identado, para que if lo detecte
```
```python
a = int(input("Dame un numero:"))
A = a % 2
if (A == 0 ):
  print(f'El numero {a} es par')

```
De esa manera sabremos que si el numero que metimos es par, pero que pasa 
si metemos un numero que no es par, si lo probamos nos damos cuenta que simplemente no pasa nada
y eso es porque nuestro programa no hace nada cuando el numero que entra es un impar, para decir que un 
numero es impar o que no es par usaremos a **else**

```python
a = int(input("Dame un numero:"))
A = a % 2
if (A == 0 ):
  print(f'El numero {a} es par')
else:
  print(f'El numero {a} no es par')
```

Si pensamos las lineas de codigo anterior como una charla, lo leeriamos de la siguiente manera:
Si el numero dado dividido entre 2 tiene un modulo igual a 0 el numero es par, de otro modo el numero 
no es par.

En este punto podemos pensar, que el else no le importara si el modulo es 1,2,3,4,5,6,7,8 
simplemente le importara si es diferente de 0, pero ¿qué pasa si tuvieramos letras que corresponden a
calificaiones?, como por ejemplo M =10 B=8 S=6 N=5. Este problema tendira varias forma de ser 
resuelto pero la manera más natural seria usando **elif**

```python
letra = input("Dame tu letra de calificación:")

if (letra == 'M' ):
  print('Tu tienes 10')
elif(letra == 'B'):
  print('Tu tienes 8')
elif(letra== 'S'):
  print('Tu tienes 6')
elif(letra=='N'):
  print('Tu tienes 5')
# Agregamos un else para hacer el programa mas robusto
#Si alguien mete alguna otra letra el programa te dice que esa letra no es valida
else:
  print('Esa letra no es valida') 
  
```
Ahora nos percatamos que si queremos probar una letra y luego otra, tendremos que correr el programa 
las veces que queramos probar nuestro código, y eso llega a ser un poco tedioso, para eliminar eso
tenemos el uso de bucles, los cuales podremos hacer que repitan líneas de código, las veces que nosotros
queramos o hasta que una condición que demos se cumpla. Para eso hablemos del ciclo while y for.


- ### While:
El ciclo while nos dará la ventaja de repetir un bloque de código, **mientras** 
la condición que nosotros hayamos declarado se cumpla. While tiene la siguiente estructura.

```python
#while(condición):
  #bloque que entrara en bucle

#es importante saber que el bloque de codigo dentro del while, debe estar identado, para que while lo detecte
```
```python
Lista = []
Y_N = 'Y'

while(Y_N == 'Y'):
  
  Lista.append(input("Dame un nombre:"))
  Y_N = input("¿Quieres meter otro nombre? Y para si, N para no: ")

print(Lista)

```
Lo que hacemos es iniciar a Y_N con un valor de Y para que nuestro ciclo while corra una primera vez, para posteriormente dentro del while poder cambiar la variable Y_N al final
, de este modo cuando el ciclo vuelva a comenzar y haga de nuevo la pregunta si Y_N es igual a Y, nosotros hayamos elegido si continuar o no.
 

- ### For:
Con el ciclo for podremos repetir un bloque de código las veces que nosotros queramos y a diferencia del while este bucle se hará las veces que nosotros queramos
sin tener que cumplir un una condicional(A menos que agreguemos una condicional if que controle a for, pero en ese caso sería mejor implementar el while).
El ciclo for tiene la siguiente estructura:

```python
#for "element "in "iteraciones": "teraciones" es una lista o array, y "n" tomara todos los valores de esa lista o array desde la posición cero hasta la final 
  #bloque que entrara en bucle

#es importante saber que el bloque de codigo dentro del for, debe estar identado, para que for lo detecte
```
ejemplo

```python
num = [1,2,3,4,5]
for n in num:
  print(n)
```
si nosotros queremos un bucle que vaya de 0 hasta el numero que queramos sin tener que hacer una lista con numeros desde el 0 hasta el numero de nuestro interes, usaremos la 
función range():

```python
#range(n) ira desde 0 hasta n-1 
#range(i,f) ira desde i hasta f-1

num = [1,2,3,4,5,6,7,8,9,10]
for n in range(5):
  print(n)#imprimimos desde el 1 hasta el 4
```
De esta manera podremos usar al ciclo for de manera muy similar a otros lenguajes de programación.
