# Imágenes RGB representadas en planos y selección de un plano específico

Para esta sección usaremos la famosa imagen de Lena, dentro de esta carpeta puedes encontrar la imagen.

![lena](https://user-images.githubusercontent.com/98423341/154170134-4ca46a31-eb33-4056-821c-546f9432b9f3.jpg)
```python
from skimage import io
import matplotlib.pyplot as plt

image = io.imread("lene.jpg") 
plt.imshow(image)

```


Descargaras la imagen y posteriormente la subiras al cuaderno para simplemente usar su nombre y extensión para subirla y visulaizarla. Como podemos observar la imagen esta a color, 
