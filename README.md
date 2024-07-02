# Minimizar-los-costes-en-el-consumo-de-energía-de-un-centro-de-datos
Deep Q-Learning

Se desarrollarán dos sistemas:
- Uno con IA y otro sin IA, por tanto, se van a calcular en paralelo dos simulaciones para ver las diferencias para poder comparar con el número de ususarios entrante y saliente, y teniendo en cuenta las variaciones de transmisión.
  
Entorno del supuesto:
- El rango óptimo de temperaturas del server variará entre 18 y 24 grados.
- La temperatura atsmosférica será el promedio durante un mes
- Temperatura mínima por la cual el servidor no funcionará será de -20 grados
- Temperatura máxima por la cual el servidor no funcionará será de 80 grados
- Número de usuarios mínimo, 10 usuarios
- Número de usuarios máximo, 100 usuarios
- Variación máxima de usuarios en el servidor por minuto será de 5 usuarios
- Tasa de transmisión de datos 20 Mbps
- Tasa de transmisión de datos 300 Mbps
- Variación máxima de transmisión de datos por minuto será de 10 Mbps

Variables:
- Temperatura del servidor en cada momento
- Cantidad de usuarios en el servidor en cada momento
- Velocidad de transmisión por minuto
- Energía gastada por la IA en el servidor (para enfriar o calentar) en cualquier momento
- Energía gastada por el sistema por el sistema de refrigeración que lleva al servidor a trabajar en su rango óptimo cada vez que la temperatura del servidor sale del rango óptimo.

Supuestos en los que se basa en módelo:

Supuesto 1: La temperatura del servidor es aproximará mediante un modelo de Regresión lineal múltiple, mediante una función lineal de la temperatura atmosférica, el número de usuarios y la velocidad de transmisión de datos.

Ejemplo: temp. servidor = temp. atmosf. + 1.25xno.de usuarios + 1.25xratio de trans. de datos

Supuesto 2: La energía gastada por un sistema (nuestra IA o el sistema de enfriamiento integrado del servidor) que cambia la temperatura del servidor de T(t) a T(t+1) en 1 unidad de tiempo (1 min), se puede aproximar mediante regresión a través de una función lineal del cambio absoluto de temperatura del servidor(al sistema le cuesta lo mismo calentar y enfriar).



