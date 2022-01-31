# Importar librerias en Python
Para llamar a una libreria que queramos usar en python deberemos usar la instrucción **import**, si usamos como ejemplo que queremos usar al valor pi, pero no queremos escribir 3.1416, podriamos importar la libreria **math** la cual contiene a la constante pi. Y en python lo escribiriamos de la siguiente manera.

```python
import math
```
Al correr esa linea automaticamente ya podremos usar al valor de pi, con lla siguiente linea de codigo

```python
math.pi 
```
El cual nos dara un valo de 3.141592653589793 pero si no queremos usar siempre la instrucción **math.pi** cada que queramos a usar al valor de pi, podemos de la libreria math solo llamar a la constante pi, dicindole a python que de nuestra libreria math solo importe a pi, en lina de codigo pedir esto, es practicamente pedirlo en ingles.

```python
from math import pi
```
Una vez teniendo esto podremos usar a pi, simplemente como pi, y ya no como math.pi.  ***Ten en cuenta que si haces esto no podras usar las demas funciones, constantes o variables de la libreria math, ya que solo importaste a pi***.

Supongamos que quieres ahora calcular el seno de algun numero, la idea sera la misma, ya sea que importes la libreria math y llames a la función seno como:

```python
import math
math.sin
```
O la llames de la siguiente manera

```python
from math import sin
```
En cualquiera de los casos tendras que llamarla como sin, si en dado caso para ti es más comodo identificar a la funcion seno, tal cual con ese nombre entonces probaras lo siguiente.
```python
from math import sin as seno
```
De esta forma podras usar a la funcion seno con ese nombre, seno y no sin.

# Libreria NUMPY
