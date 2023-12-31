import csv
from datetime import date

from . import RUTA_FICHERO


class Movimiento:
    def __init__(self, fecha, concepto, tipo, cantidad):

        self.errores = []

        try:
            self.fecha = date.fromisoformat(fecha)
        except ValueError:
            self.fecha = None
            self.errores.append(f'La fecha {fecha} no es una fecha válida')
        self.concepto = concepto
        self.tipo = tipo
        self.cantidad = cantidad

    @property
    def has_errors(self):
        return len(self.errores) > 0

    def __str__(self):
        return f'{self.fecha}\t{self.concepto}\t{self.tipo}\t{self.cantidad}\n'

    def __repr__(self):
        return self.__str__()


class ListaMovimientos:
    def __init__(self):
        self.lista_movimientos = []

    def leer_desde_archivo(self):
        self.lista_movimientos = []
        with open(RUTA_FICHERO, 'r', encoding="UTF8") as fichero:
            reader = csv.DictReader(fichero)
            for fila in reader:
                movimiento = Movimiento(
                    fila['fecha'],
                    fila['concepto'],
                    fila['ingreso_gasto'],
                    fila['cantidad']
                )
                self.lista_movimientos.append(movimiento)

    def agregar(self, fecha, concepto, tipo, cantidad):
        self.lista_movimientos.append([fecha, concepto, tipo, cantidad])
        self.lista_movimientos.sort(key=lambda item: item[0], reverse=True)
        self.guardar_archivo()

    def guardar_archivo(self):
        with open(RUTA_FICHERO, mode='w', newline="\n") as records_file:
            writer = csv.writer(records_file)
            writer.writerow(("fecha", "concepto", "tipo", "cantidad"))
            writer.writerows(self.lista_movimientos)

    def __str__(self):
        result = ''
        for mov in self.lista_movimientos:
            result += f'\n{mov}'
        return result

    def __repr__(self):
        return self.__str__()
