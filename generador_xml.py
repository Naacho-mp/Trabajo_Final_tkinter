import xml.etree.ElementTree as ET
from planta import Planta
from generador_reporte import GeneradorReporte

class GeneradorReporteXML(GeneradorReporte):
    def __init__(self, plantas=None):
        super().__init__(plantas)

    def generar_reporte(self, filename="reporte_plantas.xml"):
        root = ET.Element("plantas")

        for planta in self.plantas:
            planta_elem = ET.SubElement(root, "planta")
            ET.SubElement(planta_elem, "common_name").text = planta.common_name
            ET.SubElement(planta_elem, "scientific_name").text = planta.scientific_name
            ET.SubElement(planta_elem, "family").text = planta.family
            ET.SubElement(planta_elem, "score").text = str(planta.score)
            ET.SubElement(planta_elem, "image_path").text = planta.image_path

        self.guardar_reporte(root, filename)

    def guardar_reporte(self, root, filename):
        tree = ET.ElementTree(root)
        tree.write(filename)
        print(f"Reporte XML generado: {filename}")

    def __add__(self, planta):
        """ Sobrecarga del operador '+' para agregar una planta al reporte XML """
        if isinstance(planta, Planta):
            self.plantas.append(planta)
        return self

    def __sub__(self, planta):
        """ Sobrecarga del operador '-' para eliminar una planta del reporte XML """
        if isinstance(planta, Planta) and planta in self.plantas:
            self.plantas.remove(planta)
        return self

"""
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
"""

