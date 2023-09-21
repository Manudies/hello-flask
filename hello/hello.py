from flask import Flask

# instanciamos Flask, tenmos que pasar un nombre de app
app = Flask(__name__)


@app.route("/")
def hola():
    return "Hola soy Flask. ¿Cómo te llamas?"


@app.route("/adios")
def adios():
    return "Te dejo que tengo hambre"


@app.route("/new")
def new():
    return "Esta es una ruta nueva. Cuidado con los moradores. www.google.es"
