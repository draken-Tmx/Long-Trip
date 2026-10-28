#!/data/data/com.termux/files/usr/bin/bash
set -eu

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$PROJECT_DIR/.venv"
BIN_DIR="$HOME/.local/bin"
COMMAND="$BIN_DIR/longtrip"

echo "==> Comprobando herramientas..."

for cmd in python ffmpeg node; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "Falta instalar: $cmd"
        exit 1
    fi
done

echo "==> Creando entorno virtual..."

if [ ! -x "$VENV/bin/python" ]; then
    python -m venv "$VENV"
fi

echo "==> Instalando dependencias..."

"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install -r "$PROJECT_DIR/requirements.txt"

echo "==> Creando comando long-trip..."

mkdir -p "$BIN_DIR"

cat > "$COMMAND" <<LAUNCHER
#!/data/data/com.termux/files/usr/bin/bash
cd "$PROJECT_DIR"
exec "$VENV/bin/python" "$PROJECT_DIR/longtp.py" "\$@"
LAUNCHER

chmod +x "$COMMAND"

echo "==> Configurando fish..."

if command -v fish >/dev/null 2>&1; then
    fish -c 'fish_add_path "$HOME/.local/bin"'
fi

echo "==> Configurando zsh..."

if [ -f "$HOME/.zshrc" ]; then
    if ! grep -Fq '.local/bin' "$HOME/.zshrc"; then
        printf '\nexport PATH="$HOME/.local/bin:$PATH"\n' >> "$HOME/.zshrc"
    fi
fi

echo
echo "Instalacion completada."
echo "Ejecuta Long Trip con: longtrip"
