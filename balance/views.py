from . import app


@app.route("/")
def home():
    """
    MUestra la lista de movimientos cargados.
    """
    return "Lista de movimientos"


@app.route("/nuevo")
def add_movement():
    """
    Crea un movimiento nuevo y lo guarda en CSV
    """
    return "Agregar nuevo movimiento"


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
