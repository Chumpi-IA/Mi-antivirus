import hashlib
from flask import Flask, render_template, request

app = Flask(__name__)

# --- AQUÍ PONES LA FUNCIÓN ---
def obtener_firma_archivo(ruta_archivo):
    sha256_hash = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for bloque in iter(lambda: f.read(4096), b""):
            sha256_hash.update(bloque)
    return sha256_hash.hexdigest()
# -----------------------------

@app.route('/')
def index():
    return render_template('index.html')

# Aquí podrías crear una ruta para recibir el archivo del antivirus
@app.route('/escanear', methods=['POST'])
def escanear():
    # Lógica para recibir el archivo y usar obtener_firma_archivo()
    pass

if __name__ == '__main__':
    app.run(debug=True)
