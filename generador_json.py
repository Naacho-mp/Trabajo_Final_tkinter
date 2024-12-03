import json
from planta import Planta
from generador_reporte import GeneradorReporte

class GeneradorReporteJSON(GeneradorReporte):
    def __init__(self, plantas=None):
        super().__init__(plantas)

    def generar_reporte(self, filename="reporte_plantas.json"):
        plantas_dict = [planta.__dict__ for planta in self.plantas]
        self.guardar_reporte(plantas_dict, filename)

    def guardar_reporte(self, data, filename):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        print(f"Reporte JSON generado: {filename}")

    def __add__(self, planta):
        """ Sobrecarga del operador '+' para agregar una planta al reporte JSON """
        if isinstance(planta, Planta):
            self.plantas.append(planta)
        return self

    def __sub__(self, planta):
        """ Sobrecarga del operador '-' para eliminar una planta del reporte JSON """
        if isinstance(planta, Planta) and planta in self.plantas:
            self.plantas.remove(planta)
        return self


"""
# Ejemplo de uso
planta1 = Planta("Rosa", "Rosa rubiginosa", "Rosaceae", 0.95, "/ruta/a/imagen1.jpg")
planta2 = Planta("Tulipán", "Tulipa", "Liliaceae", 0.88, "/ruta/a/imagen2.jpg")

# Crear el generador de reporte
generador = GeneradorReporteJSON()

# Agregar plantas usando el operador +
generador = generador + planta1
generador = generador + planta2

# Generar el reporte JSON
generador.generar_reporte()

# Eliminar una planta usando el operador -
generador = generador - planta1

# Generar el reporte JSON después de eliminar una planta
generador.generar_reporte("reporte_actualizado.json")

"""