#!/data/data/com.termux/files/usr/bin/bash
set -eu

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$PROJECT_DIR/.venv"
BIN_DIR="$HOME/.local/bin"
COMMAND="$BIN_DIR/longtrip"

echo "==> Comprobando herramientas..."

for cmd in python ffmpeg; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Falta instalar: $cmd"
        pkg install "$cmd" -y
    fi
done

echo "==> Creando entorno virtual..."

if [ ! -x "$VENV/bin/python" ]; then
    python -m venv "$VENV"
fi

echo "==> Instalando dependencias..."

"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install -r "$PROJECT_DIR/requirements.txt"

echo "==> Creando comando longtrip..."

mkdir -p "$BIN_DIR"

cat > "$COMMAND" <<LAUNCHER
#!/data/data/com.termux/files/usr/bin/bash
cd "$PROJECT_DIR"
exec "$VENV/bin/python" "$PROJECT_DIR/longtp.py" "\$@"
LAUNCHER

chmod +x "$COMMAND"

echo "==> Configurando PATH..."

# bash
if [ -f "$HOME/.bashrc" ]; then
    grep -Fq '.local/bin' "$HOME/.bashrc" || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
fi

# zsh
if [ -f "$HOME/.zshrc" ]; then
    grep -Fq '.local/bin' "$HOME/.zshrc" || echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.zshrc"
fi

# fish - fish_add_path ya es permanente
if command -v fish >/dev/null 2>&1; then
    mkdir -p "$HOME/.config/fish"
    fish -c "fish_add_path $BIN_DIR" 2>/dev/null || true
fi

echo ""
echo "Instalacion completada."
echo "Ejecuta Long Trip con: longtrip"
echo "Si no te lo encuentra, hace: source ~/.bashrc"