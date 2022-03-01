# Características de una imágen digital

### Pixel

El termino pixel viene del termino "picture cell", que es español se traduce como celda de imagen. Un pixel corresponde a una imagen de 2D dimensiones(ancho y largo), y es el elemento más pequeño de una imagen digital.

![image](https://user-images.githubusercontent.com/98423341/153091484-796ccf68-7ea0-4a7a-b4d2-a6b369225921.png) [FotoNostra](https://www.fotonostra.com/digital/pixelesimagen.htm)

### Resolución 
Primero hablemos de pixeles que pueden tomar solo dos valores de intensidad 1 y 0, osea un bit o en otras palabras blanco(1) y negro(0), a esto se le llama niveles de gris.
El numero de pixeles en el ancho y largo que forma una imagen nos dara la resolución de la imagen y los valores de intensidad que esta imagen puede alcanzar nos dara el contraste, por ejemplo, en la siguiente imagen solo existen valores de blanco y negro, y si suponomes que los cuadros blancos con grises son pixeles valor 1 y lo negro valor 0, tendriamos una imagen con una resolución de 59px ancho por 65px largo. Entonces, nos damos cuenta que la imagen no tiene mucho detalles y solo se mueve en colores negro y blanco.

![image](https://user-images.githubusercontent.com/98423341/153092604-05fbf9da-248f-443e-96ab-c245bfbf71c2.png) [PNGEGG](https://www.pngegg.com/es/png-krhjf)

Si nosotros tuvieramos una imagen de 1080 px por 1080 px podriamos decir que es una alta definición, y su resolución seria lo bastante buena como para observar más detalles del lobo, pero en los mismos tonos, blanco y negro. Notemos que mientras más pixeles tengamos más detalladas y definidas veremos nuestras imagenes.

### Contraste

Ahora supongamos que cada pixel no solo tomara valores de 0 y 1 si no que cada pixel tiene información de hasta 8 bits o 1 byte, es este caso cada pixel podra tomar valores desde 0 hasta 255 niveles de gris, por lo cual el contraste de la imagen aumentaria 127 veces, pudiendo representar de manera correcta sombreados o ilumiación de una imagen. Por lo cual si unimos una buena resolución y un buen contraste tenemos una foto en blanco y negro como la siguiente.

![image](https://user-images.githubusercontent.com/98423341/153094728-08702dd9-e342-4903-9df5-53d4ac28d193.png)[xatakafoto](https://www.xatakafoto.com/opinion/como-deberia-ser-el-blanco-y-negro)

### Imagen RGB
Pero entonces ¿cómo logramos ver una imagen a color? Bueno el método más usado es el usar de tres colores a distintas intensidades cada uno para formar un color especifico, estos colores son el RGB(red, green, blue). En esta ocasión tendremos un pixel con contraste de 1 byte que tendra información en tres diferentes planos, el rojo el verde y el azul, además de cada plano tendra un valor entre 0 y 255  y al unir estos tres plano de colores primarios en ese pixel veriamos un color especifico.
Por ejemplo si en un pixel tuvieramos 0 en rojo, 0 en verde y 255 en azul, practicamente veriamos un pixel de color azul, pero si tenemos un pixel con valores de, 0 rojo, 255 verde y 255 en azul, veriamos un pixel amarillo.
Podemos darnos una idea de como se ve un pixel con RGB en la siguiente foto.

![image](https://user-images.githubusercontent.com/98423341/153095878-8b27fd75-9f3a-4bdd-bbb0-ee940320d501.png)[ionos](https://www.ionos.mx/digitalguide/paginas-web/diseno-web/que-es-un-pixel/)

### Voxel

El voxel corresponde al mínimo elemento de una imagen de 3D dimensiones(ancho, largo y profundidad) es básicamente un píxel con profundidad. 

![image](https://user-images.githubusercontent.com/98423341/156092908-41d68a38-f328-4fff-8adf-a90d3cac7444.png)

Esto se usa mucho en imágenes de resonancia magnética y tomografía computarizada, donde el voxel estará dado por su grosor de corte. Supongamos que un sujeto mide 2 metros si lo partimos a la mitad cada corte será de un metro, el grosor del corte dependerá de que tanta resolución quieras de un órgano a estudiar, mientras más cortes se tengan más resolución, el voxel es más pequeño y habrá más de estos.



