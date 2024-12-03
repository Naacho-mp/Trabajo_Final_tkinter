import xml.etree.ElementTree as ET
from planta import Planta


# Clase GeneradorReporteXML
class GeneradorReporteXML:
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

    # Método para generar el reporte XML
    def generar_reporte(self, filename="reporte_plantas.xml"):
        root = ET.Element("reporte_plantas")
        
        for planta in self.plantas:
            planta_element = ET.SubElement(root, "planta")
            ET.SubElement(planta_element, "nombre_comun").text = planta.common_name
            ET.SubElement(planta_element, "nombre_cientifico").text = planta.scientific_name
            ET.SubElement(planta_element, "familia").text = planta.family
            ET.SubElement(planta_element, "coincidencia").text = str(planta.score * 100)  # Porcentaje de coincidencia
            ET.SubElement(planta_element, "ruta_imagen").text = planta.image_path
        
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Reporte generado: {filename}")


# Ejemplo de uso
planta1 = Planta("Rosa", "Rosa rubiginosa", "Rosaceae", 0.95, "/ruta/a/imagen1.jpg")
planta2 = Planta("Tulipán", "Tulipa", "Liliaceae", 0.88, "/ruta/a/imagen2.jpg")

# Crear el generador de reporte
generador = GeneradorReporteXML()

# Agregar plantas usando el operador +
generador = generador + planta1
generador = generador + planta2

# Generar el reporte XML
generador.generar_reporte()

# Eliminar una planta usando el operador -
generador = generador - planta1

# Generar el reporte XML después de eliminar una planta
generador.generar_reporte("reporte_actualizado.xml")
