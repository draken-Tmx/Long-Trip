<div align="center">Long-Trip

How many songs does your trip last?

ES: Calculá la música que necesitás para tu próximo viaje y prepará tu playlist para el camino.

EN: Calculate how much music you need for your next trip and prepare your playlist for the road.

"Español" (#español) · "English" (#english) · "Instalación" (#instalación--installation)

</div>---

Español

Sobre el proyecto

Long-Trip es una herramienta de línea de comandos desarrollada en Python para calcular cuántas canciones necesitás durante un viaje y descargar playlists para escucharlas en el camino.

El proyecto combina el cálculo de duración musical con la descarga de audio, teniendo en cuenta un margen adicional para posibles paradas durante el trayecto.

Características actuales

- Cálculo de canciones: estimá cuántas canciones necesitás según las horas y los minutos de viaje.
- Margen para paradas: agregá un 15 % de tiempo extra al cálculo.
- Descarga de playlists: descargá el audio de una playlist mediante "yt-dlp".
- Formato MP3: convertí el audio utilizando FFmpeg.
- Metadatos y portadas: guardá metadatos e intentá incorporar la portada de cada canción.
- Directorio personalizado: elegí dónde guardar los archivos descargados.
- Interfaz de terminal: menú interactivo para acceder a las funciones disponibles.

Requisitos

- Python 3
- FFmpeg
- "yt-dlp"
- "rich"
- Node.js, para el runtime configurado de "yt-dlp"

Las dependencias de Python se gestionan mediante "requirements.txt".

Instalación

Cloná el repositorio:

git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip

Prepará el entorno e instalá las dependencias:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Asegurate de tener FFmpeg y Node.js instalados y disponibles en el sistema.

Uso

Si ejecutás el proyecto desde el repositorio:

python longtp.py

Si instalaste el comando global mediante "setup.sh", podés iniciarlo con:

long-trip

El menú permite elegir entre las siguientes opciones:

Opción| Función
"1"| Calcular las canciones necesarias para el viaje.
"2"| Descargar una playlist para el viaje.
"3"| Salir del programa.

Descarga de playlists

Al elegir la segunda opción, el programa solicita:

1. El enlace de la playlist.
2. La ruta de destino para guardar los archivos.

La descarga está configurada para guardar el audio en MP3, junto con los metadatos y las portadas cuando están disponibles.

Cookies opcionales: el programa puede utilizar un archivo local "cookies.txt" si existe en el directorio de trabajo. No compartas ni publiques cookies personales.

Estructura del proyecto

Long-Trip/
├── backend.py
├── longtp.py
├── requirements.txt
├── setup.sh
├── .gitignore
├── README.md
└── .venv/

Los archivos de configuración pueden variar según la versión instalada. El entorno ".venv" se crea localmente y no necesita incluirse en el repositorio.

Funcionalidades futuras

Estas ideas no se presentan como características implementadas:

- Interfaz visual.
- Cálculo de duración según playlists completas.
- Personalización del margen de tiempo adicional.
- Mejoras en la experiencia de usuario y los mensajes de error.

Estado del proyecto

Long-Trip está en desarrollo. Las funciones descritas como actuales corresponden al comportamiento implementado; las propuestas futuras todavía pueden cambiar.

---

English

About

Long-Trip is a Python command-line tool designed to estimate how many songs you need for a trip and download playlists for offline listening.

It combines travel-time calculations with playlist audio downloads, including an additional time allowance for possible stops.

Current features

- Song estimation: estimate the number of songs needed based on travel hours and minutes.
- Stop allowance: add a 15% time buffer to the estimate.
- Playlist downloads: download playlist audio using "yt-dlp".
- MP3 conversion: convert audio using FFmpeg.
- Metadata and artwork: save metadata and attempt to embed available artwork.
- Custom output directory: choose where downloaded files are stored.
- Interactive CLI: access available features through a terminal menu.

Requirements

- Python 3
- FFmpeg
- "yt-dlp"
- "rich"
- Node.js for the configured "yt-dlp" runtime

Python dependencies are managed through "requirements.txt".

Installation

Clone the repository:

`git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip`

Create a virtual environment and install dependencies:

`python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt`

Make sure FFmpeg and Node.js are installed and available on your system.

Usage

Run the project directly:

`python longtp.py`

If you installed the global command through `setup.sh`, launch it with:

`long-trip`

The interactive menu provides three options:

Option| Function
"1"| Estimate the songs needed for your trip.
"2"| Download a travel playlist.
"3"| Exit the program.

Playlist downloads

When selecting the second option, enter the playlist URL and the destination directory.

The downloader is configured to save audio as MP3 and include metadata and artwork when available.

An optional local "cookies.txt" file can be used if present in the working directory. Never publish or share personal cookies.

Planned features

The following are ideas for future development, not implemented features:

- Graphical user interface.
- Playlist-based duration calculations.
- Customizable travel-time allowance.
- Improved user experience and error handling.

Project status

Long-Trip is under development. Future functionality may change as the project evolves.

---

License

No license has been specified here. Check the repository for an existing license before redistributing or reusing the project.

Author

DrakenTMX

"GitHub Repository" (https://github.com/draken-Tmx/Long-Trip)

---

<div align="center">Made for the road. Powered by music.

</div>
