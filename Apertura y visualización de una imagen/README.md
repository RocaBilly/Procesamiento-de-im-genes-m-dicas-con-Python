# Apertura y visualización de una imagen

Para abrir una imagen con simplemente debemos importar la librería skimage y de ella importar a io, io nos dará la posibilidad de crear un objeto tipo array de 8 bits, esto quiere 
decir que al ser una imagen la máxima su contraste irá de 0 a 255 niveles de intensidad. Posteriormente deberemos llamar al método pyplot de matplotlib, para de esta manera poder
visualizar la imagen que hayamos cargado.

```python
from skimage import io
import matplotlib.pyplot as plt
```
Una vez teniendo estas librerias guardaremos nuestro objeto tipo array en una variable llamada image, usando io.imread("Nombre de la imagen.estensión") de esta manera a la variable image se le guardaran valores numericos que corresponden a la intensidad de cada pixel, y para poder visualizar la imagen usaremos el metodo imshow(variable con la imagen), de la libreria matplotlib.


```python
image = io.imread("Logo.png") 
plt.imshow(image)
```

*Nota: en mi caso la imagen se llama Logo y es de extensión png*

Mi imagen Logo es la siguiente: ![image](https://user-images.githubusercontent.com/98423341/153920229-492560d7-4199-4f37-8bc8-0a7062cf9e47.png)

Y una vez subida a colab y abierta con skimage, se vera de la siguiente manera:
![image](https://user-images.githubusercontent.com/98423341/153920342-9ba94956-5fd3-4b07-9ad3-594629e5e5c3.png)

Si nosotros usaramos el print para ver la imagen, lo que veriamos serian algunos de los valores del array creado, en vez de la imagen.

![image](https://user-images.githubusercontent.com/98423341/153922397-d197c865-a023-4b76-92f0-955d9ea4da21.png)
