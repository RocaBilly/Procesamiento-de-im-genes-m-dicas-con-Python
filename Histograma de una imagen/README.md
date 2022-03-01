# Histograma de una imagen

Un histograma nos dará información sobre los niveles de intensidad de los píxeles de forma gráfica, así podremos darnos cuenta si la imagen está demasiado iluminada o muy oscura y de ser posible ecualizar la imagen.

```python
from skimage import io
import matplotlib.pyplot as plt
import numpy as np
import cv2

image = io.imread("lena.jpg") 
plt.imshow(image)
```
El método que se usara, tendra los sigueinte parametros: cv2.calcHsit(imagen,plano de color,mascara,maximo nivel de intensidad del histograma, Rango de valores de intensidad). la mascara sera una región especifica de la imagen.

```python
hist = cv2.calcHist([image], [0], None, [256], [0, 256])
plt.plot(hist, color='gray' )

plt.xlabel('Nivel de intensidad')
plt.ylabel('Cantidad de piexeles ')
plt.show()

plt.imshow(image[:,:,0],cmap=plt.cm.gray)
```

En este caso estamos viendo el plano rojo y el numero de pixeles que tiene cada nivel de intensidad, desde el 0 hasta el 255.

![histLena](https://user-images.githubusercontent.com/98423341/156261477-66ef0966-38a6-46aa-815f-58469a3827bf.png)

De esta manera podemos apreciar que los valores altos de intensidad predominan en el plano rojo.

Comparemos los histogramas de cada plano RGB.

Con el siguiente codigo podremos compararlos en una misma grafica

```python
color = ('r','g','b')

for i in range(len(color)):

    hist = cv2.calcHist([image], [i], None, [256], [0, 256])
    plt.plot(hist, color = color[i])
    plt.xlabel('Nivel de intensidad')
    plt.ylabel('Cantidad de piexeles ')
    plt.xlim([0,256])

plt.show()
plt.imshow(image)
```
Deberemos ver lo siguiente: 

![Histo LENA](https://user-images.githubusercontent.com/98423341/156263499-35f173a6-963a-4ebe-85f5-8d56baffe821.png)

Y con el siguiente codigo podremos ver por separado cada histograma


```python
color = ('r','g','b')
COLOR =('HistRed','HistGreen','HistBlue')
HIST = []

fig, axes = plt.subplots(1,3, figsize=(12, 8))
ax = axes.ravel()
for i in range(len(color)):
    HIST.append(cv2.calcHist([image], [i], None, [256], [0, 256]))

for i in range(len(color)):
    ax[i].plot(HIST[i], color = color[i])
    ax[i].set_title(COLOR[i])


fig.tight_layout()
plt.show() 

```

![image](https://user-images.githubusercontent.com/98423341/156264102-c8ff77f3-75f2-4ce1-b072-90bba4092481.png)

