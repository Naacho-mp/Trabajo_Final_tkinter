from fpdf import FPDF
from planta import Planta

# Clase GeneradorReportePDF
class GeneradorReportePDF:
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

    # Método para generar el reporte PDF
    def generar_reporte(self, filename="reporte_plantas.pdf"):
        pdf = FPDF(orientation="P", unit="mm", format="Letter")
        pdf.add_page()

        # Agregar título al documento
        self.agregar_titulo(pdf, "Informe de Plantas", 80, 20)

        diff_y = 40  # Empezamos a escribir en el eje Y

        for planta in self.plantas:
            # Agregar información de cada planta
            self.agregar_texto(pdf, f"Best Match: {planta.score*100:.2f}%", 20, diff_y)
            self.agregar_imagen(pdf, planta.image_path, 20, diff_y + 5, 50, 55)
            self.agregar_texto(pdf, f"Nombre común: {planta.common_name}", 75, diff_y + 15)
            self.agregar_texto(pdf, f"Nombre Científico: {planta.scientific_name}", 75, diff_y + 25)
            self.agregar_texto(pdf, f"Familia: {planta.family}", 75, diff_y + 35)

            diff_y += 70  # Desplazar hacia abajo para la siguiente planta

        # Guardar el PDF generado
        pdf.output(filename)
        print(f"Reporte PDF generado: {filename}")

    def agregar_titulo(self, pdf, titulo, x, y, font_size=16):
        pdf.set_font('Arial', '', font_size)
        pdf.text(x, y, txt=titulo)

    def agregar_texto(self, pdf, texto, x, y, font_size=12):
        pdf.set_font('Arial', '', font_size)
        pdf.text(x, y, txt=texto)

    def agregar_imagen(self, pdf, imagen, x, y, w, h):
        try:
            pdf.image(imagen, x, y, w, h)
        except Exception as e:
            print(f"Error al agregar imagen: {e}")

# Ejemplo de uso
planta1 = Planta("Rosa", "Rosa rubiginosa", "Rosaceae", 0.95, "C:/Users/nicol/Desktop/5519240445_8746faf3f0_z.jpg")
planta2 = Planta("Tulipán", "Tulipa", "Liliaceae", 0.88, "C:/Users/nicol/Desktop/5519240445_8746faf3f0_z.jpg")

# Crear el generador de reporte
generador = GeneradorReportePDF()

# Agregar plantas usando el operador '+'
generador = generador + planta1
generador = generador + planta2

# Generar el reporte PDF
generador.generar_reporte()

# Eliminar una planta usando el operador '-'
generador = generador - planta1

# Generar el reporte PDF después de eliminar una planta
generador.generar_reporte("reporte_actualizado.pdf")
