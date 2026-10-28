# Long Trip
¿Cuantas canciones dura tu viaje?
-----------------------------------
# ¿Que es long Trip?

- ¿ Eres de esas personas que viajan mucho y escuchan musica la mitad del dia?, entonces Long Trip es para ti.


- Es un programa de terminal que calcula el tiempo de viaje en canciones para que no gastes datos ni mucho menos gastes almacenamiento sin sentido.

  
- Tiene un diseño agradable y básico para usuarios no tan experimentados.


- ¿ Entones dime, cuantas canciones dura tu viaje ?


# Funciones

- **Calculadora de viaje:** estima la cantidad de canciones necesarias para un viaje y un margen de tiempo adicional para paradas o inconvenientes.

- **Descarga Playlist:** Descarga canciones en MP3 mediante yt-dlp y FFmpeg. 

- **Guardado:** Guarda las canciones con el nombre de su playlist y organizadas en numeros.

- **Menu interactivo:** Ingresa las opciones desde el menú principal.


# Requisitos. 

- `yt-dlp`
- `Python 3`
- `rich`
- `FFmpeg`
- `Node.js configurado como entorno de Javascrip para Yt-dlp`
- `git para clonar el repositorio`

# Instalación.

**Clona el repositorio:** 

- `git clone https://github.com/draken-Tmx/long-trip.git`

**Entra a la carpeta:** 

- `cd long-trip`

**Instala las dependencias:**

- `pkg update
pkg install python ffmpeg nodejs git`

**Ejecutar el instalador:**

- `chmod +x setup.sh
./setup.sh`


# USO. 

- Una vez instalado ejecuta:
`longtrip` desde la terminal, el lanzador utiliza automáticamente el entorno venv y ejecuta el archivo, no necesitas hacer `Venv` manualmente. 



# opciones. 

**El menu ofrece un total de 3 opciones**
 - Calcular tiempo de viaje en canciones. 
 - Descargar playlist.
 - salir del programa


# Calculo del tiempo de viaje. 

La calculadora utiliza una duración promedio de cancion de **3 minutos con 40 segundos** y agrega un margen del 15% para paradas e inconvenientes en el viaje.

*El resultado es una estimación del viaje, no es una calculacion exacta, abstente a ser un tonto* 


# Descarga de playlist. 

El descargador utiliza *yt-dlp* y *FFmpeg* para extraer el audio y convertirlo a MP3 en maxima calidad, procesar los metadatos y extraer las miniaturas disponibles. 


# Estructura del proyecto. 

Long-Trip/

├── backend.py       
├── longtp.py        
├── requirements.txt 

├── setup.sh         
├── .gitignore       
└── README.md 


# Próximas funciones. 

*Actualmente el programa está en desarrollo e iré agregando y mejorando funciones a medida del tiempo, sepan entender*


# Final.

*si el repositorio te gustó o te resultó interesante, te agradecería mucho que le dejes una estrella* <3


Creador [Draken-Tmx](https://github.com/draken-Tmx)



