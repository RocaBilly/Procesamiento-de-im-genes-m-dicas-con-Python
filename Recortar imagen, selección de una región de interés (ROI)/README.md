# Recortar imagen, selección de una región de interés (ROI)


Ya sabemos que una imagen no es más que una matriz, por lo cual si nosotros quisiéramos una región específica de la imagen, tendríamos que hacer una submatriz de la matriz de la imagen.

Por suerte al visualizar la imagen nos da una idea de dónde recortar.

![image](https://user-images.githubusercontent.com/98423341/156266751-d5bed116-4e6e-4787-a635-c0f5070b95bb.png) Si quierieramos solo la cara de Lena, podriamos hacer el corte en los siguientes valores, los cuales son los indices de nuestra matriz, o los pixeles de la imagen.

![image](https://user-images.githubusercontent.com/98423341/156267350-bbe65bbc-f6d6-45f1-8e4b-101840d5fec5.png) 

Desde el indice 200 hasta 500 en largo y el 200 hasta 500 en ancho.
Entonces crearemos una subMatriz con esos valores y después la visualizaremos. 

```python
subIm = image[200:500,200:500,:] #Podemos ver que es muy facil delimitar nuestra región de interes.
#Y si queremos la imagen a color, el recorte debera hacerse en los tres planos  
plt.imshow(subIm)
```
![image](https://user-images.githubusercontent.com/98423341/156267749-53bb7301-3d88-4bda-88d9-f133aab78ed6.png)

De esta manera podremos analizar una zona especifica de la imagen o eliminar partes que no nos interesen de la imagen.

