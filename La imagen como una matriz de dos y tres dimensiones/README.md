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

Pero si habláramos de voxeles, ¿cómo veríamos nuestra imagen?.
Como se mencionó antes, el voxel estará dado por el grosor del corte o SLice(en el ámbito de imagenología médica), por lo cual si son muchos cortes, los voxeles serán más delgados o si son pocos cortes, los voxeles será más gruesos.
Volvamos de nuevo al ejemplo de partir a una persona a la mitad y supongamos que la imagen 2D de esta persona es de 255x255px, pero solo vemos a la persona desde arriba y solo veremos la punta de su cabeza, si ahora partimos a la mitad a la persona, tendremos  dos cortes o planos para ver al sujeto, donde además de solo ver la punta de la cabeza podremos ver lo que hay a la mitad de su cuerpo en una imagen de igual tamaño 255x255px.
Si bien partimos al sujeto en 10 tendríamos 10 planos de nuestro sujeto, cada uno de 255x255px y veríamos diferentes alturas de su cuerpo, no solo su cabeza ni la mitad de su cuerpo.
Por lo cual en Python, podremos ver a una matriz de 3 dimensiones como  varias matrices de 2 dimensiones, donde cada una nos dará información diferente sobre nuestra imagen volumétrica.
Una matriz de 255x255(Ancho y largo)x10(número de planos corte) la veríamos como una variable de la siguiente manera.

 ```python
im3D = np.ones((255,255,10))       
```
![image](https://user-images.githubusercontent.com/98423341/156094945-05d7fcd2-9031-4d14-8943-bfc94790c7c0.png)

En este caso son 10 imagenes de 255x255px donde todos sus valores son 1
