# Imágenes RGB representadas en planos y selección de un plano específico

Para esta sección usaremos la famosa imagen de Lena, dentro de esta carpeta puedes encontrar la imagen.

![lena](https://user-images.githubusercontent.com/98423341/154170134-4ca46a31-eb33-4056-821c-546f9432b9f3.jpg)

```python
from skimage import io
import matplotlib.pyplot as plt

image = io.imread("lene.jpg") 
plt.imshow(image)
```


Descargaras la imagen y posteriormente la subiras al cuaderno para simplemente usar su nombre y extensión para subirla y visulaizarla. Como podemos observar la imagen esta a color, en este caso sabemos que es una imagen RGB ya que contiene 3 planos de color, esto lo podemos corroborar explorando nuestros variables de nuestro cuaderno.

![image](https://user-images.githubusercontent.com/98423341/155230387-2cbc50a7-2dc6-4409-b0fc-27f188f1871b.png)

Vemos que la imagen es de 630 píxeles x 630 píxeles y contiene tres planos. Pero a diferencia de una imagen 3D estos planos no son cortes de diferentes partes del sujeto, sino que cada plano son niveles de intensidad para cada plano RGB. Ya que recordemos que a una imagen a color la hace la suma de estos 3 colores.

Ahora con la misma imagen visualizaremos las intensidades de cada plano.


```python
red = image[:,:,0] #Dejamos ver toda la imagen, pero solo del plano 0 el cual es el plano de intesidades rojo
green = image[:,:,1] #Dejamos ver toda la imagen, pero solo del plano 0 el cual es el plano de intesidades Green
blue = image[:,:,2] #Dejamos ver toda la imagen, pero solo del plano 0 el cual es el plano de intesidades Blue

fig, axes = plt.subplots(2, 2, figsize=(12, 8)) #hacemos una cuadricula de 2 por dos imagenes, para tener las 
#intensidades de cada plano la imagen original

ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title("Original")
ax[1].imshow(red,cmap=plt.cm.gray) # La parte importante de este linea de codigo es plt.cm.gray
#mapear los valores en un plano de intensidades de Gris
ax[1].set_title("Red")
ax[2].imshow(green,cmap=plt.cm.gray)
ax[2].set_title("Green")
ax[3].imshow(blue,cmap=plt.cm.gray)
ax[3].set_title("Blue")

fig.tight_layout()
plt.show()
```
![image](https://user-images.githubusercontent.com/98423341/156098417-f5af4f7a-f26e-49fb-8d38-bc7ec9fccebb.png)

Podemos ver que el plano de los rojos tiene más intensidad y tiene sentido ya que a simple vista la imagen original, se ve muy cálida. 

Ahora si bien queremos ver la imagen en rojo en azul o en verde, haremos lo siquiente.

```python
red = np.copy(image) #Haremos una copia de la imagen original
green = np.copy(image)
blue = np.copy(image)

#Para el plano rojo  los demas planos los mandaremos a 0
red[:,:,1]=0 
red[:,:,2]=0

#Para el plano verde los demas planos los mandaremos a 0
green[:,:,0]=0
green[:,:,2]=0

#Para el plano azul  los demas planos los mandaremos a 0
blue[:,:,0]=0
blue[:,:,1]=0


fig, axes = plt.subplots(2, 2, figsize=(12, 8))
ax = axes.ravel()

ax[0].imshow(image)
ax[0].set_title("Original")
ax[1].imshow(red)
ax[1].set_title("Red")
ax[2].imshow(green)
ax[2].set_title("Green")
ax[3].imshow(blue)
ax[3].set_title("Blue")

fig.tight_layout()
plt.show()
```


![image](https://user-images.githubusercontent.com/98423341/156100167-7bbb9516-71fc-47d2-ac7f-56feb28d0c85.png)

De estas dos maneras, podemos ver las intensidades de cada plano, o separa a cada plano. 



