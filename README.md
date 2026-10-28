<a id="readme-top"></a>

<!-- PROJECT SHIELDS -->""Python" (https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)" (https://www.python.org/)
""yt-dlp" (https://img.shields.io/badge/yt--dlp-audio%20downloader-000000?style=for-the-badge)" (https://github.com/yt-dlp/yt-dlp)
""GitHub stars" (https://img.shields.io/github/stars/draken-Tmx/Long-Trip?style=for-the-badge)" (https://github.com/draken-Tmx/Long-Trip/stargazers)
""GitHub issues" (https://img.shields.io/github/issues/draken-Tmx/Long-Trip?style=for-the-badge)" (https://github.com/draken-Tmx/Long-Trip/issues)

<!-- PROJECT TITLE --><br /><div align="center">Long Trip

¿Cuántas canciones dura tu viaje?

A Python CLI tool to estimate your trip's soundtrack and download playlists for offline listening.

Una herramienta CLI en Python para calcular la banda sonora de tu viaje y descargar playlists para escucharlas sin conexión.

"Explore the Project" (https://github.com/draken-Tmx/Long-Trip)
·
"Report a Bug" (https://github.com/draken-Tmx/Long-Trip/issues)
·
"Request a Feature" (https://github.com/draken-Tmx/Long-Trip/issues)

</div>---

<!-- TABLE OF CONTENTS --><details>
  <summary><strong>Table of Contents / Índice</strong></summary>  <ol>
    <li><a href="#about-the-project">About the Project / Sobre el proyecto</a></li>
    <li><a href="#features">Features / Funcionalidades</a></li>
    <li><a href="#built-with">Built With / Tecnologías</a></li>
    <li><a href="#getting-started">Getting Started / Instalación</a></li>
    <li><a href="#usage">Usage / Uso</a></li>
    <li><a href="#project-structure">Project Structure / Estructura</a></li>
    <li><a href="#roadmap">Roadmap / Próximamente</a></li>
    <li><a href="#license">License / Licencia</a></li>
    <li><a href="#contact">Contact / Contacto</a></li>
  </ol>
</details>---

<!-- ABOUT THE PROJECT -->About the Project

Long Trip is a command-line project built with Python. It helps estimate how many songs you may need for a trip and provides a way to download playlists for offline listening.

The project combines a simple travel-time calculator with a playlist downloader in one interactive terminal menu.

Sobre el proyecto

Long Trip es un proyecto de línea de comandos desarrollado en Python. Permite estimar cuántas canciones podrías necesitar para un viaje y descargar playlists para escucharlas sin conexión.

El proyecto combina una calculadora de tiempo de viaje con un descargador de playlists en un menú interactivo.

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- FEATURES -->Features

- Travel calculator: estimates the number of songs needed for a trip.
- Playlist downloader: downloads playlist audio and converts it to MP3.
- Organized downloads: stores tracks in a playlist-named folder with numbered filenames.
- Interactive CLI: access the available features through a terminal menu.
- Virtual environment: isolates Python dependencies with "venv".
- Setup script: automates environment creation and Python dependency installation.

Funcionalidades

- Calculadora de viaje: estima la cantidad de canciones necesarias para un viaje.
- Descargador de playlists: descarga audio y lo convierte a MP3.
- Descargas organizadas: guarda las canciones en una carpeta con el nombre de la playlist y archivos numerados.
- Menú interactivo: permite acceder a las funciones desde la terminal.
- Entorno virtual: mantiene aisladas las dependencias de Python mediante "venv".
- Instalador: automatiza la creación del entorno y la instalación de dependencias.

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- BUILT WITH -->Built With

Technology| Purpose
"Python" (https://www.python.org/)| Application logic
"yt-dlp" (https://github.com/yt-dlp/yt-dlp)| Playlist and media downloading
"FFmpeg" (https://ffmpeg.org/)| Audio conversion and metadata processing
"Rich" (https://github.com/Textualize/rich)| Terminal interface and status display
"Node.js" (https://nodejs.org/)| JavaScript runtime used by the current "yt-dlp" configuration

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- GETTING STARTED -->Getting Started

Follow these steps to install Long Trip on Termux.

Prerequisites

Install the required system packages:

pkg update
pkg install python ffmpeg nodejs git

Installation

1. Clone the repository

git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip

2. Run the setup script

chmod +x setup.sh
./setup.sh

The setup script checks for the required tools, creates the ".venv" virtual environment, installs the dependencies from "requirements.txt", and creates the "long-trip" launcher in "~/.local/bin".

Instalación en español

Seguí estos pasos para instalar Long Trip en Termux.

1. Instalar las herramientas necesarias

pkg update
pkg install python ffmpeg nodejs git

2. Clonar el repositorio

git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip

3. Ejecutar el instalador

chmod +x setup.sh
./setup.sh

El instalador comprueba las herramientas necesarias, crea el entorno virtual ".venv", instala las dependencias de "requirements.txt" y genera el comando "long-trip" en "~/.local/bin".

«Note / Nota: The current backend uses a Termux-specific Node.js path. Other environments may require a configuration change.

El backend utiliza actualmente una ruta de Node.js específica de Termux. En otros entornos puede ser necesario modificarla.»

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- USAGE -->Usage

After installation, launch Long Trip from your terminal:

long-trip

The launcher runs the application using the project's virtual environment. Manual activation is not required.

Menú principal

Option| Function
"1"| Measure travel time / Calcular tiempo de viaje
"2"| Download a playlist / Descargar una playlist
"3"| Exit / Salir

Travel Calculator / Calculadora de viaje

The current calculation uses an average song duration of 3 minutes and 40 seconds and adds a 15% time allowance to the trip duration.

La calculadora utiliza una duración promedio de 3 minutos y 40 segundos y agrega un margen del 15 % al tiempo del viaje.

«Results are estimates. The calculator does not currently analyze the actual duration of a playlist's tracks.

Los resultados son estimaciones. Actualmente, la calculadora no analiza la duración real de las canciones de una playlist.»

Playlist Downloader / Descargador de playlists

Provide a playlist URL and a destination directory when prompted. The downloader uses "yt-dlp" and FFmpeg to process the audio and convert it to MP3.

Ingresá el enlace de la playlist y la ruta de destino cuando el programa lo solicite. El descargador utiliza "yt-dlp" y FFmpeg para procesar el audio y convertirlo a MP3.

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- PROJECT STRUCTURE -->Project Structure

Long-Trip/
├── backend.py
├── longtp.py
├── requirements.txt
├── setup.sh
├── .gitignore
└── README.md

File| Description
"backend.py"| Calculation and download functions
"longtp.py"| Main CLI menu
"requirements.txt"| Python dependencies
"setup.sh"| Environment setup and launcher creation
".gitignore"| Files excluded from Git
"README.md"| Project documentation

Estructura del proyecto

- "backend.py": funciones de cálculo y descarga.
- "longtp.py": menú principal de la CLI.
- "requirements.txt": dependencias de Python.
- "setup.sh": creación del entorno e instalación.
- ".gitignore": archivos excluidos de Git.
- "README.md": documentación del proyecto.

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- ROADMAP -->Roadmap

Long Trip is a work in progress. Future features will be listed here as development goals are defined.

Long Trip continúa en desarrollo. Las próximas funcionalidades se agregarán a medida que se definan los objetivos del proyecto.

- [ ] Define and document future features / Definir y documentar futuras funcionalidades.
- [ ] Improve portability beyond Termux / Mejorar la compatibilidad con otros entornos.

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- LICENSE -->License

No license has been specified yet.

Todavía no se especificó una licencia para el proyecto.

<p align="right"><a href="#readme-top">Back to top ↑</a></p><!-- CONTACT -->Contact

Developer: "draken-Tmx" (https://github.com/draken-Tmx)

Project Link: "Long Trip on GitHub" (https://github.com/draken-Tmx/Long-Trip)

Issues and suggestions: "Open an issue" (https://github.com/draken-Tmx/Long-Trip/issues)

<p align="right"><a href="#readme-top">Back to top ↑</a></p>---

<div align="center">Developed by "draken-Tmx" (https://github.com/draken-Tmx)

Built for the road, powered by music.

Hecho para el camino, impulsado por la música.

</div>
