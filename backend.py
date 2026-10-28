import yt_dlp
import subprocess
import os
from rich.console import Console


console=Console()

class NoLog:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass
    def info(self, msg): pass

def limpiar():
    console.clear()


def obtener_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"
    return None

def viaje():
    print("ingrese su tiempo de viaje") 
    horas=int(input("horas: "))
    min_extra=int(input("minutos: "))
    cancion=3+40/60
    tasa=0.15
    tiempo=horas*60 + min_extra
    tiempo_con_tasa=tiempo*(1+tasa)
    canciones=tiempo_con_tasa/cancion
    print(f"tiempo de viaje {horas}hs con {min_extra}min.")
    print(f"canciones necesarias {round(canciones)}")
    print(f"canciones sin tasa de paradas {round(tiempo/cancion)}")

def animacion(funcion, *args, mensaje=""):
    with console.status(f"{mensaje}", spinner="dots"):
        return funcion(*args)


def descarga_viaje():
    limpiar()
    try:
        url = input("link de la PLAYLIST: ")
        audio_path=input("ingrese su ruta de destino. (ej: /storage/musica/): ")
        os.makedirs(audio_path, exist_ok=True)
        yt_opts = {
            "format": "bestaudio/best",
            "noplaylist": False, 
            "yes_playlist": True,
            "outtmpl": f"{audio_path}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
            "quiet": True,
            "no_color":True,
            "no_progress":True,
            "logger":NoLog(),
            "no_warnings": True,
            "writethumbnail": True,
            "postprocessors": [
                {
                    "key": "FFmpegExtractAudio",
                    "preferredcodec": "mp3",
                    "preferredquality": "0",
                },
                {
                    "key": "FFmpegThumbnailsConvertor",
                    "format": "jpg",
                },
                {
                    "key": "EmbedThumbnail",
                },
                {
                    "key": "FFmpegMetadata",
                }
            ],
            "js_runtimes": {"node": {"path": "/data/data/com.termux/files/usr/bin/node"}},
            "remote_components": ["ejs:github"],
        }
        cookies = obtener_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animacion(ydl.download, [url], mensaje="Descargando playlist...")

        console.print(f"✓ Playlist completa")
        console.input('Enter para salir')
    except Exception as e:
        print(e)
