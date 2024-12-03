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
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    #AGREGAR Título
    agregar_titulo(pdf, 'Informe de Plantas', 80, 20)

    diff_y = 40  # Empezamos a escribir en el eje Y
    margen_inferior = 270 

    for planta in plantas:
        if diff_y + 50 > margen_inferior:
            pdf.add_page()
            diff_y = 20

        agregar_texto(pdf, f"Nombre común: {planta.common_name}",20, diff_y)
        agregar_imagen(pdf, planta.image_path, 20, diff_y + 5, 50, 55)
        agregar_texto(pdf, f'Best Match {planta.score}',75, diff_y + 35 ) 
        agregar_texto(pdf, f"Nombre Cientifico: {planta.scientific_name}", 75, diff_y + 15)
        agregar_texto(pdf, f"Familia: {planta.family}",75, diff_y + 25 )
                                                                                                    
        diff_y += 80  

    # GUARDAR
    pdf.output('Informe_plantas.pdf')

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
    
    crear_pdf(plantas)
