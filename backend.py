import yt_dlp
import subprocess
import os
from rich.console import Console
import json


console=Console()

class NoLog:
    def debug(self, msg): pass
    def warning(self, msg): pass
    def error(self, msg): pass
    def info(self, msg): pass

def clear():
    console.clear()


def get_cookies():
    if os.path.exists("cookies.txt"):
        return "cookies.txt"
    return None

def journey():
    try:
        clear()
        print("Enter your travel time.") 
        hour=int(input("hours: "))
        min_extra=int(input("minutes: "))
        song=3+40/60
        rate=0.15
        time=horas*60 + min_extra
        time_with_rate=time*(1+enter_route)
        songs=time_with_rate/song
    
        print("")
        print(f"travel time {horas}hs-{min_extra}min.")
        print("")
        print(f"necessary songs: {round(songs)}")
        print("")
        print(f"songs without a stop rate: {round(time/song)}")
        print("")
        input("Enter to return.")
    except ValueError as e:
        print("only numbers")

def animation (function, *args, message=""):
    with console.status(f"{message}", spinner="dots"):
        return function(*args)

path_dw = "path.json"

def get_route():
    if os.path.exists(path_dw):
        with open(path_dw, "r", encoding="utf-8") as f:
            config=json.load(f)
            print(f"route loaded automatically: {config[path_dw]}")
            return config[path_dw]
    else:
        while True:
            enter_route =input("Enter the route for the first time: ").strip()

            if os.path.exists(enter_route):
                config ={path_dw: enter_route}
                with open(path_dw,"w",encoding="utf-8") as f:
                    json.dump(config,f,indent=4)

                print("saved")
                return enter_route
            else:
                print("error")

def trip_download(): # descarga viaje
    clear()
    try:
        url = input("Playlist link: ")
        route_final=get_route()
        yt_opts = {
            "format": "bestaudio/best",
            "noplaylist": False, 
            "yes_playlist": True,
            "outtmpl": f"{route_final}/%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s",
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
        cookies = get_cookies()
        if cookies:
            yt_opts["cookiefile"] = cookies

        with yt_dlp.YoutubeDL(yt_opts) as ydl:
            animation(ydl.download, [url], message="Downloading playlist...")

        console.print(f"✓ Playlist completed")
        console.input('Enter to exit')
    except Exception as e:
        print(e)


