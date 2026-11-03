#!/data/data/com.termux/files/usr/bin/bash
set -eu

PROJECT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$PROJECT_DIR/.venv"
BIN_DIR="$HOME/.local/bin"
COMMAND="$BIN_DIR/longtrip"

echo "==> Checking tools..."

for cmd in python ffmpeg; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "need to install: $cmd"
        pkg install "$cmd" -y
    fi
done

echo "==> Creating virtual environment..."

if [ ! -x "$VENV/bin/python" ]; then
    python -m venv "$VENV"
fi

echo "==> Installing dependencies..."

"$VENV/bin/python" -m pip install --upgrade pip
"$VENV/bin/python" -m pip install -r "$PROJECT_DIR/requirements.txt"

echo "==> Creating command longtrip..."

mkdir -p "$BIN_DIR"

cat > "$COMMAND" <<LAUNCHER
#!/data/data/com.termux/files/usr/bin/bash
cd "$PROJECT_DIR"
exec "$VENV/bin/python" "$PROJECT_DIR/longtp.py" "\$@"
LAUNCHER

chmod +x "$COMMAND"

echo "==> Configuring PATH..."

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
echo "Installation completed."
echo "Execute Long Trip with: longtrip"
echo "if you can't find it, do: source ~/.bashrc"