from flask import render_template

from . import app
from .models import ListaMovimientos


@app.route("/")
def home():
    """
    Muestra la lista de movimientos cargados.
    """
    lista = ListaMovimientos()
    lista.leer_desde_archivo()

    return render_template('inicio.html', movs=lista.lista_movimientos)


@app.route("/nuevo")
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en CSV
    """
    return render_template("nuevo.html")


@app.route("/modificar")
def update():
    """
    Permite crear los datos de un movimiento creado previamente
    """
    return "Actualizar movimiento"


@app.route("/borrar")
def delete():
    """
    Borra un movimiento existente
    """
    return "Borrar un movimiento"
