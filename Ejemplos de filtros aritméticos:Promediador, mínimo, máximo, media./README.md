# Ejemplos de filtros aritméticos:Promediador(Media), mediana.

Tendremos dos tipos de filtros espaciales, los Lineales y los no lineales. En esta sección hablaremos de los filtros lineales ya que básicamente estos son los basados en un kernel de convolución.

## Filtro de Media o Promediador

Este filtro busca reducir las variaciones entre los píxeles de un vecindario, dejando a todos los valores en un valor promedio. De este modo se eliminaran los ruidos tales como el sal y pimienta en donde hay valores de pixeles con intensidad muy baja(negros) o muy alta(blancos). Para este filtro al igual que los demás haremos uso del kernel de convolución.




