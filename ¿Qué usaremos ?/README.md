# ¿Qué usaremos ?

![image](https://user-images.githubusercontent.com/98423341/153906098-3c8ef95f-4966-4387-86ad-5e5dc8f19b30.png)

En esta parte final y enfocada del curso, usaremos scikit-image lo cual es una colección de algoritmos para el procesamiento de imágenes. 
Está disponible de forma gratuita y libre de restricciones.
Además usaremos también al famoso openCv de python que esta diseñada para resolver problemas de visión por computadora.

![image](https://user-images.githubusercontent.com/98423341/156265207-c329d98d-32df-458e-b329-e078f001c285.png)

En este caso necesitaremos instalar estas librerias antes de importarla, por lo cual dejaremos usar replit y en cambio usaremos google colab:

![image](https://user-images.githubusercontent.com/98423341/153907793-175ca45a-40d0-4225-aa93-6f8a5af4c7e9.png)[Colab](https://colab.research.google.com/) nos permite programar 
en python en una maquina externa a la nuestra y poder instalar librerias, subir archivos y descargar archivos. Veamos un pequeño recorrido sobre colab. Una vez entrando a la pagina
principal de colab veremos lo siguente:
![image](https://user-images.githubusercontent.com/98423341/153908477-ae21898a-36d7-4e07-a303-1ee5f18bfdc4.png) 

*Nota: debemos tener una cuenta de gmail*

Le daremos a archivo y escogeremos **nuevo cuaderno** ![image](https://user-images.githubusercontent.com/98423341/153909019-ed8bf483-675a-451f-96b5-f3fbe6e90b69.png) y una vez 
teniendo un nuevo cuaderno abierto tendremos algo cómo lo siguiente:

![image](https://user-images.githubusercontent.com/98423341/153909235-2c9d33a8-4fc1-4b6b-83ee-3257aff2115d.png)

En esta parte trabajaremos de ahora en adelante. Bien como se mencionó al inicio deberemos instalar el scikit-image(es posible que ya este instalado),simplemente usaras la siguiente
linea de codigo:

```python
pip install scikit-image
pip install opencv-python
```
Una vez teniendo esa linea de codigo le daras click en el pay, se te asignará una servidor para que programes y ya podrás empezar a usar la libreria skimage 

![image](https://user-images.githubusercontent.com/98423341/153910567-64ddf54a-0a54-4135-b869-d8b3921a58c6.png)
![image](https://user-images.githubusercontent.com/98423341/156265781-ec2feb58-ba64-40a6-ad9a-59667e41326a.png)

 Podríamos tener todo el programa dentro de una sola celda, pero para tener un orden te recomiendo uses varias celdas, donde cada celda podría ser una parte del programa y así 
 tener más control de este. Para agregar una nueva celda de codigo daras clic en **+ Código** 
 ![image](https://user-images.githubusercontent.com/98423341/153911366-ec76c3b0-0345-46af-a538-fec0bccc96d1.png)
 
 Por último lo que debemos saber, ya que deberemos usar imágenes, ya sea abrirlas o guardarlas en nuestra computadora, veremos donde subir archivos en colab, para eso presionaremos en el apartado izquierda **Archivo** una vez ahi tendremos dos opciones, subir la foto directamente desde tu computadora(amarillo), pero sera temporal o que colab entre a tu drive(verde) y de ahi subir la imagen al cuaderno y también guardarla en tu drive. 
 
![image](https://user-images.githubusercontent.com/98423341/153912949-555f37ec-8686-4487-83d8-7e62cf4db489.png) Para este curso subiremos las imágenes que necesitemos(amarillo), ya que no nos interesa que estén ahí siempre, además así será más fácil leerlas y guardarlas.






