import json
from planta import Planta

# Clase GeneradorReporteJSON
class GeneradorReporteJSON:
    def __init__(self, plantas=None):
        # Si no se pasa ninguna lista, inicializa una lista vacía
        self.plantas = plantas if plantas is not None else []

    # Sobrecarga del operador '+' para agregar una planta
    def __add__(self, planta):
        if isinstance(planta, Planta):
            self.plantas.append(planta)
        return self

    # Sobrecarga del operador '-' para eliminar una planta
    def __sub__(self, planta):
        if isinstance(planta, Planta) and planta in self.plantas:
            self.plantas.remove(planta)
        return self

    # Método para generar el reporte JSON
    def generar_reporte(self, filename="reporte_plantas.json"):
        plantas_dict = []
        
        for planta in self.plantas:
            planta_info = {
                "nombre_comun": planta.common_name,
                "nombre_cientifico": planta.scientific_name,
                "familia": planta.family,
                "coincidencia": planta.score * 100,  # Porcentaje de coincidencia
                "ruta_imagen": planta.image_path
            }
            plantas_dict.append(planta_info)
        
        with open(filename, "w") as json_file:
            json.dump(plantas_dict, json_file, indent=4)
        
        print(f"Reporte generado: {filename}")


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
