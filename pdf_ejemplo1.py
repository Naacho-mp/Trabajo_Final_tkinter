from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="Letter")
pdf.add_page()

#Para agregar texto TITULO
pdf.set_font('Arial', '', 16)
pdf.text(x=80, y=20, txt= 'Informe de Plantas')

#Para agregar texto PLANTA 1
pdf.set_font('Arial', '', 16)
pdf.text(x=20, y=40, txt= 'Best Match "imagen_1"')

#Para agregar imagenes 1
pdf.image('planta7.jpg',
          x=20, y=50, 
          w=50, h=55)

#Para agregar texto 2_Nombre
nombre = "Nombre:"

pdf.set_font('Arial', '', 12)
pdf.text(x=75, y=60, txt= nombre)

#Para agregar texto 3_Nombre Cientifico
nombre_cientifico = "Nombre Cientifico:"

pdf.set_font('Arial', '', 12)
pdf.text(x=75, y=70, txt= nombre_cientifico)

#Para agregar texto 4_Descripcion
descripcion = "Descripcion:"
pdf.set_font('Arial', '', 12)
pdf.text(x=75, y=80, txt= "Descripción: ")

#------------------------------------------#
#PLANTA 2
#Imagen 2

#Para agregar texto
pdf.set_font('Arial', '', 16)
pdf.text(x=20, y=130, txt= 'Best Match "imagen_2"')

#Para agregar imagenes 2
pdf.image('planta6.jpg',
          x=20, y=140, 
          w=50, h=55)

#Para agregar texto 2_Nombre
nombre2 = "Nombre:"

pdf.set_font('Arial', '', 12)
pdf.text(x=75, y=150, txt= nombre2)

#Para agregar texto 3_Nombre Cientifico
nombre_cientifico2 = "Nombre Cientifico:"

pdf.set_font('Arial', '', 12)
pdf.text(x=75, y=160, txt= nombre_cientifico2)

#Para agregar texto 4_Descripcion
descripcion2 = "Descripcion:"
pdf.set_font('Arial', '', 12)
pdf.text(x=75, y=170, txt= descripcion2)


pdf.output('hoja.pdf')