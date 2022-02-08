# Funciones 
Si nosotros quisiéramos usar un bloque de código cada que lo necesitemos sin tener que escribirlo cada que lo usemos, podremos crear una función y correspondiente a ese bloque de código, 
por lo cual usaremos la palabra reservada **def** de Python para crear una función.


```python
#def nombre de la función (parametro,parametro):
  #bloque de codigo
  #return valor / si es necesario
 ```
 
 Ahora vemos como seria una función que recibe y que regresa parametros.
 
 
```python
def suma(A,B):
  suma = A+B
  return suma

A=10
B=20

resultado = suma(A,B)
print(resultado)
```

Si ahora quisieramos la misma función pero que no regrese ningun resultado, pero si nos muestra el resultado de nuestra suma:


```python
def suma(A,B):
  print(A+B)

A=10
B=20

suma(A,B)

```

El usar o no, el regreso de un valor dependera de el uso que quieras darle a tu función, además puedes regresar los valores que necesites, por ejemplo


```python
def suma_resta(A,B):
  suma = A+B
  resta = A-B
  return suma,resta

A=10
B=20

Rsuma , Rresta = suma_resta(A,B)

print(Rsuma)
print(Rresta)
```

De esta manera podras crear funciones tan complejas como las necesites además de retornar valores que consideres necesarios.

