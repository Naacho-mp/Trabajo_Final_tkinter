from fpdf import FPDF

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
def crear_pdf(name,name2, name_cien, name_cien2, descrip, descrip2):
    pdf = FPDF(orientation="P", unit="mm", format="Letter")
    pdf.add_page()

    #AGREGAR Título
    agregar_titulo(pdf, 'Informe de Plantas', 80, 20)

    # AGREGAR INFO Planta 1
    agregar_texto(pdf, 'Best Match "imagen_1"', 20, 40)
    agregar_imagen(pdf, 'planta7.jpg', 20, 50, 50, 55)
    agregar_texto(pdf, f"Nombre: {name}", 75, 60)
    agregar_texto(pdf, f"Nombre Cientifico: {name_cien} ", 75, 70)
    agregar_texto(pdf, f"Descripción: {descrip}", 75, 80)

    # AGREGAR INFO Planta 2
    agregar_texto(pdf, 'Best Match "imagen_2"', 20, 130)
    agregar_imagen(pdf, 'planta6.jpg', 20, 140, 50, 55)
    agregar_texto(pdf, f"Nombre: {name2}", 75, 150)
    agregar_texto(pdf, f"Nombre Cientifico:{name_cien2}", 75, 160)
    agregar_texto(pdf, f"Descripción:{descrip2}", 75, 170)

    # GUARDAR
    pdf.output('hoja2.pdf')

if __name__ == "__main__" :
    nombre1  = "copihue"
    nombre_cient = "asd copifues"
    descr = "flor nacional de Chile"

    nombre2 = "rosa"
    nombre_cient2 = "rosaleus"
    descr2 = "rosa de color x y demases"
    
    crear_pdf(nombre1,nombre2,nombre_cient, nombre_cient2, descr, descr2)
