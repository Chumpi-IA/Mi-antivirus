from flask import Flask, render_template, request
import os
import hashlib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/escanear', methods=['POST'])
def escanear():
    ruta = request.form['ruta']
    # Aquí iría tu lógica potente de detección
    if os.path.exists(ruta):
        archivos = os.listdir(ruta)
        resultado = f"Escaneados {len(archivos)} archivos en {ruta}. Sistema Limpio."
    else:
        resultado = "La ruta no existe."
    
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
