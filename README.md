<p align="center">
  <img src="assets/logo.png" alt="Long Trip" width="120" />
</p>

<h1 align="center">🚗 Long Trip</h1>

<p align="center">
  <strong>¿Cuántas canciones dura tu viaje?</strong><br/>
  Calculá cuántas canciones necesitás para un viaje y descargá playlists para escucharlas sin conexión.
</p>

<p align="center">
  <a href="#english">English</a> · <a href="#español">Español</a>
</p>

<p align="center">
  <img alt="Python" src="https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white" />
  <img alt="FFmpeg" src="https://img.shields.io/badge/FFmpeg-Required-FC6222" />
  <img alt="Platform" src="https://img.shields.io/badge/Platform-Termux-555555" />
  <img alt="Status" src="https://img.shields.io/badge/Status-WIP-orange" />
</p>

---

## 📖 Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Roadmap](#roadmap)
- [License](#license)

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 🧮 **Travel calculator** | Estimates the number of songs based on trip duration (avg. 3m 40s + 15% margin) |
| 🎵 **Playlist downloader** | Downloads playlist audio via `yt-dlp` and converts to MP3 with metadata |
| 📁 **Organized files** | Saves tracks in a playlist-named folder with numbered filenames |
| 💻 **Interactive CLI** | Simple terminal menu to access all features |
| 🐍 **Virtual environment** | Isolated Python dependencies via `venv` |

## 📋 Requirements

| Tool | Purpose |
|------|---------|
| Python 3.10+ | Application runtime |
| FFmpeg | Audio conversion and metadata processing |
| Node.js | JavaScript runtime for `yt-dlp` |
| Git | Clone the repository |

## 🚀 Installation

**1. Clone the repository**

```bash
git clone https://github.com/draken-Tmx/Long-Trip.git
cd Long-Trip

2. Install system dependencies (Termux)

pkg update
pkg install python ffmpeg nodejs git

3. Run the setup script

chmod +x setup.sh
./setup.sh

[!NOTE]
The setup script creates the .venv virtual environment, installs dependencies from requirements.txt, and registers the long-trip command in ~/.local/bin.

🎮 Usage
Launch from any directory:

long-trip

Main Menu
Option	Action
1	Calculate songs needed for a trip
2	Download a playlist
3	Exit

Travel Calculator
The calculator uses:

Average song duration: 3 min 40 s
Additional time margin: 15%
[!WARNING]
Results are estimates. The calculator does not currently analyze the actual duration of playlist tracks.

Playlist Downloader
Uses yt-dlp + FFmpeg to:

Extract audio from playlist tracks
Convert to MP3
Process available metadata and thumbnails
[!TIP]
If a cookies.txt file exists in the project directory, it will be used automatically for authenticated downloads.

📁 Project Structure
Long-Trip/
├── backend.py          # Calculation and download functions
├── longtp.py           # Main CLI menu
├── requirements.txt    # Python dependencies
├── setup.sh            # Environment setup script
├── .gitignore
└── README.md

⚙️ Configuration
The setup script requires python, ffmpeg, and node in PATH.
The backend currently uses a Termux-specific Node.js path.
If cookies.txt exists in the project directory, it is used for downloads.
[!CAUTION]
Never commit private cookies to GitHub.

🗺️ Roadmap
[ ] Analyze actual playlist track durations
[ ] Add custom song duration per user
[ ] Support multiple platforms (Linux, macOS, Windows)
[ ] Add export to file (CSV/JSON)
[ ] Add unit tests
