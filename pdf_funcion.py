from fpdf import FPDF
from testCard import Planta

# instalar el fpdf : pip install fpdf

#TITULO
def agregar_titulo(pdf, titulo, x, y, font_size = 16):
    pdf.set_font('Arial', '', font_size)
    pdf.text(x, y, txt=titulo)

#BEST MATCH
def agregar_texto(pdf, texto, x, y, font_size=12):
    pdf.set_font('Arial', '', font_size)
    pdf.text(x, y, txt=texto)

#"AGREGAR IMAGEN"
def agregar_imagen(pdf, imagen, x, y, w, h):
    pdf.image(imagen, x, y, w, h)

#CREAR EL PDF
def crear_pdf(plantas):
    pdf = FPDF(orientation="P", unit="mm", format="Letter")
    pdf.add_page()

    #AGREGAR Título
    agregar_titulo(pdf, 'Informe de Plantas', 80, 20)

    y_offset = 40  # Empezamos a escribir en el eje Y

    for planta in plantas:
        # Agregar información de la planta
        agregar_texto(pdf, f'Best Match "{planta.score}"', 20, y_offset)
        agregar_imagen(pdf, planta.image_path, 20, y_offset + 10, 50, 55)
        agregar_texto(pdf, f"Nombre común: {planta.common_name}", 75, y_offset + 60)
        agregar_texto(pdf, f"Nombre Cientifico: {planta.scientific_name}", 75, y_offset + 70)
        agregar_texto(pdf, f"Descripción: {planta.family}", 75, y_offset + 80)

        y_offset += 100

    # GUARDAR
    pdf.output('hoja2.pdf')

if __name__ == "__main__" :

    plantas = [ 
        Planta(
            common_name="Chilean-bellflower",
            scientific_name="Lapageria rosea Ruiz & Pav.",
            family="Philesiaceae",
            score=0.80134,
            image_path="planta6.jpg"  
        ),
        Planta(
            common_name="dadasdasda",
            scientific_name="Lapageria rosea Ruiz & Pav.",
            family="Philesiaceae",
            score=0.80134,
            image_path="planta7.jpg"  
        )        
    ]


    nombre1  = "copihue"
    nombre_cient = "asd copifues"
    descr = "flor nacional de Chile"

    nombre2 = "rosa"
    nombre_cient2 = "rosaleus"
    descr2 = "rosa de color x y demases"
    
    crear_pdf(plantas)
