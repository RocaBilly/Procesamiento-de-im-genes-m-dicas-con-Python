# La imagen como una matriz de dos y tres dimensiones

Nosotros podemos ver a una imagen de dos dimensiones, como una matriz que tiene tantas columnas como píxeles de ancho la imagen, y tantas filas como píxeles de largo.
Veamos un ejemplo. 


![pixel](https://user-images.githubusercontent.com/98423341/156089180-9f04386f-9ab9-48c6-beb7-da544378e3a6.png)

 Si pensamos en ese arreglo de píxeles como una imagen podríamos pensar en una imagen que tendrá una resolución de 4px por 4px. Si además fuera una imagen que tiene 8 bits en contraste, entonces cada píxel sólo podría tener un valor de 0 o 255. Por lo cual tendríamos una matriz de 4x4, y como podemos notar los pixeles son grises, entonces lo valores de cada valor de la matriz estarían en un valor medio de contraste, 128 aproximadamente. Vamos a crear esta matriz en python y visualizarla como una imagen.
 
Cómo se necesita una referencia de cual es el valor mas negro y cual el más blanco, haremos una imagenes con diferentes tonos de grises, para poder apresiar a la matriz de 4x4 y cada uno de sus pixeles.

 
 ```python
import matplotlib.pyplot as plt
import numpy as np
 
imagen = np.array([[128, 129,130,131], [132,133, 134,135], [136,137, 138,149], [151,160, 161,190]],dtype=np.uint8)
plt.imshow(imagen,cmap=plt.cm.gray)
```
Veremos cómo esa matriz de 4x4 se ve como una imagen de 4x4 px.

![image](https://user-images.githubusercontent.com/98423341/156091694-8a5c6251-721c-4ce7-a99b-2216315112e5.png)

Pero si habláramos de voxeles, ¿cómo veríamos nuestra imagen?
