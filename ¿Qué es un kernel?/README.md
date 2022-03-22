# ¿Qué es un kernel y filtro espacial?

Antes de hablar de los filtros espaciales (basados en kernels o máscaras de convolución) y filtros lineales y no lineales. Hablaremos de que es un kernel o máscara.
Un kernel o máscara de convolución puede entenderse como una matriz de coeficientes que al ser aplicada en un píxel objetivo se obtiene una transformación en el píxel objetivo, usando a sus píxeles vecinos.

Pero que son los vecinos de un pixel. Generalmente los píxeles de interés estarán al centro de nuestro kernel, por lo cual solo hablaremos de kernels cuadrados.

![image](https://user-images.githubusercontent.com/98423341/157088091-e04ebce4-a50d-49b5-8de2-3640ec548f06.png)

Si nuestro pixel de interes es el pixel azul con la letra e, sus vecinos son todos los pixeles dentro de ese kernel de color verde.
Pero un kernel también puede tener una dimensión de 4x4 o 5x5 y todos los píxeles que estén dentro del kernel y no sean el pixel de interés, serán los vecinos.

## Convolución
Hay unas cosas más antes de hablar de filtros en las imágenes, debemos entender que es una convolución usando un kernel. La convolución nos dará una transformación en el pixel de interés, haciendo la suma de las multiplicaciones de los píxeles de la imagen que estén dentro de la dimensión del kernel(ventana), multiplicados con los píxeles del kernel. Veamos un ejemplo: 
![image](https://user-images.githubusercontent.com/98423341/157089701-eae4cd98-7043-4da9-8d98-3764f62e980b.png)

Tenemos un kernel que será aplicado a un píxel que tiene un valor 1(azul), entonces las operaciones que se harán serán sobre los píxeles dentro de la misma dimensión del kernel. Las operaciones serían las siguientes. (0)(1)+(-1)(3)+(0)(2)+(-1)(2)+(5)(1)+(-1)(0)+(0)(1)+(-1)(3)+(0)(2), dando como resultado un valor de -3 por lo cual el valor de la transformación en ese píxel sería, -3 pero para que sea una transformación completa deberá aplicarse esta máscara a toda la imagen y hacer esta convolución pixel por pixel, pero qué pasa con los pixeles de las orillas de la imagen, si nuestro kernel más pequeño cuadrado es de dimensión 3x3, en los pixeles de las orillas, no tendremos los vecinos suficientes para hacer una convolución en este pixel. Lo cual nos lleva a otro concepto a tratar.

## Padding 

![image](https://user-images.githubusercontent.com/98423341/157094718-9204e6c3-fd13-4210-beb3-ee01d75588af.png)

Como notamos en la imagen al aplicar el kernel(verde con amarillo) en valores de la orilla en nuestra imagen nos faltaran valores y al no tener ninguna valor Python nos lanzará un error, para eso existe algo llamado padding lo cual es como un marco, que se le agrega a la imagen original según el tamaño del kernel, con un kernel de 3x3 será un marco de un píxel alrededor de la imagen, en un kernel de 4x4 será un marco de 2 pixeles y así sucesivamente. 

El marco puede ser de la siguiente manera:
-  un marco de 0, esto es llamado Zero padding.
- Agregar un marco de valores que son los mismo que el de los bordes.

El zero paddin lo usaremos cuando el borde de tu imagen no tenga información importante y el otro marco se usara cuando el borde de la imagen sea tan importante como lo demás. Ahora ya sabemos que es un kernel y una convolución, a continuación veremos como usamos estas dos nuevas herramientas, para filtrar o mejorar nuestra imagen.

## Filtro Espacial

Un filtro espacial trabaja directamente en los valores del píxel de la imagen, usando un kernel de convolución o algunas otras técnicas.
Los principales objetivos de un filtro son los siguientes:
- Suavizar la imagen: Reducir variaciones abruptas de intensidad entres los pixeles vecinos
- Realzar la imagen: Aumentar variaciones abruptas de intensidad entres los pixeles vecinos
- Eliminar ruido: Modificar píxeles vecinos de un vecindario que salgan totalmente de los valores normales, o comunes de la vecindad.
- Detectar bordes: Detección del borde de una imagen, teniendo en cuenta que el borde de una imagen, los píxeles tienen un cambio abrupto de intensidades 


