# app.py
from flask import Flask
from flask import render_template

# Creamos la aplicación
app = Flask(__name__)

# Nuestros datos (como una mini base de datos)
CITAS = {
    1: {
        "autor": "Albert Einstein",
        "texto": "La imaginación es más importante que el conocimiento."
    },
    2: {
        "autor": "Steve Jobs",
        "texto": "Tu tiempo es limitado, así que no lo malgastes viviendo la vida de otra persona."
    },
    3: {
        "autor": "Nelson Mandela",
        "texto": "Siempre parece imposible hasta que se hace."
    }
}

# --- Definimos las Rutas (Páginas) ---

# 1. Página de Inicio (muestra la lista de todas las citas)
@app.route("/")
def index():
    # 'index.html' será nuestra plantilla
    # le pasamos la variable 'citas' para que el HTML pueda usarla
    return render_template("index.html", citas=CITAS)

# 2. Página de Cita Individual (usa una URL dinámica)
# <int:id> significa que aceptará un número en la URL (ej: /cita/1)
@app.route("/cita/<int:id>")
def ver_cita(id):
    # Obtenemos la cita específica del diccionario
    cita = CITAS.get(id)
    
    # Si la cita no existe, podríamos mostrar un error
    if not cita:
        return "Cita no encontrada", 404
        
    # 'cita.html' será la plantilla
    # le pasamos la variable 'cita'
    return render_template("cita.html", cita=cita)

# --- Esto es para ejecutar la aplicación ---
if __name__ == "__main__":
    # El modo debug se reinicia solo cuando guardas cambios
    app.run(debug=True)