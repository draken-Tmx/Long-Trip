Long Trip

How many songs does your trip last?

Long Trip is a Python CLI project designed to help estimate how many songs you may need for a trip and download playlists for offline listening.

It provides an interactive terminal menu with two main features: travel-time calculation and playlist downloading.

Features

- Travel time calculator: estimates the number of songs needed based on trip duration.
- Playlist downloader: downloads playlist audio and converts it to MP3 using "yt-dlp" and FFmpeg.
- Organized downloads: stores tracks in a folder named after the playlist, with track numbers in filenames.
- Interactive CLI: access the available features through a terminal menu.
- Virtual environment: isolates Python dependencies using "venv".
- Setup script: automates environment creation and dependency installation.

Requirements

- Python 3
- FFmpeg
- Node.js
- Git, to clone the repository

The Python dependencies are listed in "requirements.txt".

Installation

1. Install system dependencies

On Termux:

pkg update
pkg install python ffmpeg nodejs git

On other operating systems, install Python, FFmpeg, and Node.js using the appropriate package manager or official installers.

2. Clone the repository

git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip

3. Run the setup script

chmod +x setup.sh
./setup.sh

The script checks for the required system tools, creates the ".venv" virtual environment, installs the Python dependencies, and creates the "long-trip" launcher in "~/.local/bin".

Usage

After installation, run Long Trip from the terminal:

long-trip

The launcher uses the project's virtual environment automatically. You do not need to activate ".venv" manually.

The interactive menu provides three options:

1. Measure travel time: enter the trip duration in hours and additional minutes to estimate the number of songs needed.
2. Download a playlist: provide a playlist URL and a destination directory.
3. Exit: close the application.

Travel time calculation

The current calculator uses an average song duration of 3 minutes and 40 seconds and adds a 15% time allowance to the trip duration.

These values produce an estimate; the calculator does not currently measure the actual duration of a playlist.

Playlist downloading

The downloader uses "yt-dlp" and FFmpeg to extract audio, convert it to MP3, and process available metadata and thumbnails.

Downloaded tracks are organized into a playlist-named directory, with track numbers included in filenames.

Project Structure

Long-Trip/
├── backend.py       # Calculation and download functions
├── longtp.py        # Main CLI menu
├── requirements.txt # Python dependencies
├── setup.sh         # Environment setup script
├── .gitignore       # Excluded files
└── README.md        # Project documentation

The ".venv/" directory is generated during setup and should not be committed to Git.

Configuration Notes

- The setup script expects "python", "ffmpeg", and "node" to be available in the system "PATH".
- The current backend uses a Termux-specific Node.js path. Other environments may require adjusting this configuration.
- If "cookies.txt" exists in the project directory, the downloader uses it. Otherwise, it proceeds without a cookie file.
- Keep cookie files private and never commit them to the repository.

Roadmap

Long Trip is a work in progress. Additional features will be documented here as development goals are defined and implemented.

Project Status

The project is under active development. Features and configuration may change as development continues.

---

Long Trip — Español

¿Cuántas canciones dura tu viaje?

Long Trip es un proyecto de Python con interfaz de línea de comandos (CLI) que permite estimar cuántas canciones podrías necesitar para un viaje y descargar playlists para escucharlas sin conexión.

Ofrece un menú interactivo con dos funciones principales: calcular el tiempo de viaje y descargar playlists.

Funcionalidades

- Calculadora de viaje: estima la cantidad de canciones necesarias según la duración del viaje.
- Descargador de playlists: descarga audio y lo convierte a MP3 mediante "yt-dlp" y FFmpeg.
- Descargas organizadas: guarda las canciones en una carpeta con el nombre de la playlist y agrega el número de pista al nombre de cada archivo.
- Menú interactivo: permite acceder a las funciones desde la terminal.
- Entorno virtual: mantiene aisladas las dependencias de Python mediante "venv".
- Instalador automático: crea el entorno e instala las dependencias del proyecto.

Requisitos

- Python 3
- FFmpeg
- Node.js
- Git, para clonar el repositorio

Las dependencias de Python están definidas en "requirements.txt".

Instalación

1. Instalar las dependencias del sistema

En Termux:

pkg update
pkg install python ffmpeg nodejs git

En otros sistemas operativos, instalá Python, FFmpeg y Node.js mediante el gestor de paquetes correspondiente o sus instaladores oficiales.

2. Clonar el repositorio

git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip

3. Ejecutar el instalador

chmod +x setup.sh
./setup.sh

El script comprueba las herramientas necesarias, crea el entorno virtual ".venv", instala las dependencias de Python y genera el lanzador "long-trip" en "~/.local/bin".

Uso

Una vez instalado, ejecutá Long Trip desde la terminal:

long-trip

El lanzador utiliza automáticamente el entorno virtual del proyecto. No necesitás activar ".venv" manualmente.

El menú interactivo ofrece tres opciones:

1. Calcular tiempo de viaje: ingresá la duración del viaje en horas y minutos adicionales para estimar la cantidad de canciones necesarias.
2. Descargar una playlist: ingresá el enlace de la playlist y el directorio de destino.
3. Salir: cerrar la aplicación.

Cálculo del tiempo de viaje

La calculadora utiliza una duración promedio de canción de 3 minutos y 40 segundos y agrega un margen del 15 % al tiempo del viaje.

El resultado es una estimación: actualmente, la calculadora no mide la duración real de una playlist.

Descarga de playlists

El descargador utiliza "yt-dlp" y FFmpeg para extraer el audio, convertirlo a MP3 y procesar los metadatos y las miniaturas disponibles.

Las canciones se organizan en una carpeta con el nombre de la playlist y se identifican mediante números de pista en sus nombres de archivo.

Estructura del proyecto

Long-Trip/
├── backend.py       # Funciones de cálculo y descarga
├── longtp.py        # Menú principal de la CLI
├── requirements.txt # Dependencias de Python
├── setup.sh         # Instalador del entorno
├── .gitignore       # Archivos excluidos de Git
└── README.md        # Documentación del proyecto

El directorio ".venv/" se genera durante la instalación y no debe subirse al repositorio.

Notas de configuración

- El instalador necesita que "python", "ffmpeg" y "node" estén disponibles en el "PATH" del sistema.
- El backend utiliza actualmente una ruta de Node.js específica de Termux. En otros entornos puede ser necesario modificarla.
- Si existe un archivo "cookies.txt" en el directorio del proyecto, el descargador lo utiliza. De lo contrario, continúa sin ese archivo.
- Mantené los archivos de cookies en privado y nunca los subas al repositorio.

Próximas funciones

Long Trip continúa en desarrollo. Las nuevas funcionalidades se documentarán a medida que se definan los objetivos y se implementen.

Estado del proyecto

El proyecto está en desarrollo activo. Las funcionalidades y la configuración pueden cambiar a medida que avance el desarrollo.

---

Developed by "draken-Tmx" (https://github.com/draken-Tmx).
