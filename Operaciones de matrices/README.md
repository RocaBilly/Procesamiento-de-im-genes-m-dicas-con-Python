# Operaciones de matrices 

Con python y numpy podemos hacer todas las operaciones que son posibles de hacer con una matriz. Tales como suma y resta, 
Multiplicación por un escalar, multiplicación con una matriz(respetando las normas de la multiplicación matricial), multiplicación con otra matriz punto a punto, traspuesta de una matriz,
divisiones por un escalar, división con otra matriz punto a punto. 
A Continuación veremos las funciones que nos permiten realizar estas operaciones:

```python
import numpy as np #traspuesta

A = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(f'Array A sin trasponer \n {A}')

At = A.T
print(f'Array A traspuesta \n {At}')
```

```python
import numpy as np #Multiplicación de matrices 

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,1],[2,2],[3,3]])

print(A.dot(B)) #A*B

#Multiplicación con un escalar

escalar =10 
A = np.array([[1,2],[3,4]])
print(A*escalar)

# Multiplicación punto a punto

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,1,1],[2,2,2]])

print(A*B)
```

```python
import numpy as np #Suma y resta

A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,1,1],[2,2,2]])

print(A+B)
print(A-B)
```

```python
import numpy as np #División  


#División con un escalar

escalar = 10 
A = np.array([[1,2],[3,4]])
print(A/escalar)

#Division con matriz punto a punto
A = np.array([[1,2,3],[4,5,6]])
B = np.array([[1,1,1],[2,2,2]])

print(A/B)
