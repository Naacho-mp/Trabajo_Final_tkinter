from planta import Planta
from generador_pdf import GeneradorReportePDF
from generador_json import GeneradorReporteJSON
from generador_xml import GeneradorReporteXML


# Crear plantas de ejemplo
planta1 = Planta("Rosa", "Rosa rubiginosa", "Rosaceae", 0.95, "c:/Users/nicol/Desktop/5519240445_8746faf3f0_z.jpg")
planta2 = Planta("Tulipán", "Tulipa", "Liliaceae", 0.88, "c:/Users/nicol/Desktop/5519240445_8746faf3f0_z.jpg")

# Crear generador para PDF
generador_pdf = GeneradorReportePDF()
generador_pdf + planta1  # Agregar planta al generador
generador_pdf + planta2  # Agregar otra planta
generador_pdf.generar_reporte("reporte_plantas.pdf")

# Crear generador para JSON
generador_json = GeneradorReporteJSON()
generador_json + planta1  # Agregar planta al generador
generador_json + planta2  # Agregar otra planta
generador_json.generar_reporte("reporte_plantas.json")

# Crear generador para XML
generador_xml = GeneradorReporteXML()
generador_xml + planta1  # Agregar planta al generador
generador_xml + planta2  # Agregar otra planta
generador_xml.generar_reporte("reporte_plantas.xml")