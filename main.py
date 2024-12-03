import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from planta import Planta
from plant_card import PlantCard
from analizador_imagenes import AnalizadorPlantas

from generador_pdf import GeneradorReportePDF
from generador_json import GeneradorReporteJSON
from generador_xml import GeneradorReporteXML

def cargar_imagen():
    image_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.jpg;*.jpeg;*.png")])
    return image_path

def cambiar_color():
    ventana.config(bg="chartreuse2")

def analizar():
    global image_path  # Aquí es donde almacenamos la ruta de la imagen cargada
    if image_path:
        analizador = AnalizadorPlantas()
        planta = analizador.analizar_imagen(image_path)
        if planta:
            card = PlantCard(ventana, planta, bg="#f0f0f0", width=250, height=300)
            card.grid(row=6, column=0, padx=150, pady=15)

# Función que se llama cuando se hace clic en el botón de cargar imagen
def cargar_y_mostrar_imagen():
    global image_path
    image_path = cargar_imagen()

def generar_reporte_xml():
    try:
        ruta = entrada.get()
        analizador = AnalizadorPlantas()
        plantas = analizador.obtener_plantas_por_directorio(ruta)
        reporte = GeneradorReporteXML()
        for planta in plantas:
            reporte = reporte + planta
        reporte.generar_reporte()
        messagebox.showinfo("Reporte generado", "El reporte se ha generado correctamente")
    except Exception as ex:
        messagebox.showerror("Error", f"Ha habido una excepción: {type(ex).__name__}\n{ex}")

def generar_reporte_pdf():
    try:
        ruta = entrada.get()
        analizador = AnalizadorPlantas()
        plantas = analizador.obtener_plantas_por_directorio(ruta)
        reporte = GeneradorReportePDF()
        for planta in plantas:
            reporte = reporte + planta
        reporte.generar_reporte()
        messagebox.showinfo("Reporte generado", "El reporte se ha generado correctamente")
    except Exception as ex:
        messagebox.showerror("Error", f"Ha habido una excepción: {type(ex).__name__}\n{ex}")

def generar_reporte_json():
    try:
        ruta = entrada.get()
        analizador = AnalizadorPlantas()
        plantas = analizador.obtener_plantas_por_directorio(ruta)
        reporte = GeneradorReporteJSON()
        for planta in plantas:
            reporte = reporte + planta
        reporte.generar_reporte()
        messagebox.showinfo("Reporte generado", "El reporte se ha generado correctamente")
    except Exception as ex:
        messagebox.showerror("Error", f"Ha habido una excepción: {type(ex).__name__}\n{ex}")

def seleccionar_directorio():
    ventana.filename = filedialog.askdirectory()
    entrada.delete(0, tk.END)
    entrada.insert(0, ventana.filename)


ventana = tk.Tk() # Acá tenemos nuestro objeto ventana. Es propio del paquete.␣

ventana.title("Plant Review") # Este es un método
ventana.geometry("1280x720") # Dimensiones
ventana.minsize(100, 100)
ventana.maxsize(1280, 720)
ventana.iconbitmap("icono_plant.ico") # Agregar un icono
ventana.configure(bg="White")

ventana.geometry("1280x720+100+8") # Podemos agregar las coordenadas
ventana.attributes("-alpha", 1.0) # Controlar la opacidad
ventana.resizable(True, True) #Bloque de la ventana 

#ETIQUETAS
titulo = tk.Label(ventana, text="🌱 Plant Review 🍂")
titulo.config(fg="black", bg="OliveDrab1", anchor= "w", font=("Times New Roman", 16, "bold"))
titulo.grid(row=0, column=0, padx=20, pady=15, sticky="w")  

sub_titulo = tk.Label(ventana, text="Sube tu imagen (planta, arbusto, hierba o flor)")
sub_titulo.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 14, "bold"))
sub_titulo.grid(row=1, column=0, padx=25, pady=15, sticky="w")  

#FRAME 
frame1 = tk.Frame(ventana) 
frame1.configure(width=430, height=90, bg='gray85')
frame1.grid(row=2, column=0, padx=20, pady=5) 

#BOTON SUBIR IMAGEN
boton = tk.Button(ventana, text="Subir ⬆", width=10, height=1, command=cargar_y_mostrar_imagen)
boton.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10))
boton.grid(row=2, column= 0)

#BOTON 2
boton2 = tk.Button(ventana, text="Analizar 🔎", width=10, height=1, command=analizar)
boton2.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton2.grid(row=3, column= 0, sticky="w", padx=340)

#Resultados titulo
resultados = tk.Label(ventana, text="Resultados - Análisis")
resultados.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 16, "bold"))
resultados.grid(row=4, column=0, padx=25, pady=5, sticky="w")

#FRAME IMAGEN
frame_imagen = tk.Frame(ventana) 
frame_imagen.configure(width=450, height=100, bg='gray85')
frame_imagen.grid(row=6, column=0, padx=150, pady=15)

#TITULO 2
titulo_2 = tk.Label(ventana, text="Analizar Directorio")
titulo_2.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 16, "bold"))
titulo_2.grid(row=0, column=1, padx=45, pady=5, sticky="we")  

#SUBTITULO DIRECTORIO
sub_titulo_2 = tk.Label(ventana, text="Ruta del Directorio")
sub_titulo_2.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 14))
sub_titulo_2.grid(row=1, column=1, padx=45, pady=5, sticky="w")  

#ENTRADA DIRECTORIO
entrada = tk.Entry(ventana)
entrada.config(fg = "black", bg="gray85", font=("Arial", 12))
entrada.grid(row=2, column=1, padx=35, sticky="e")

#BOTON ANALIZAR DIRECTORIO
boton3 = tk.Button(ventana, text="Seleccionar carpeta", width=15, height=1, command=seleccionar_directorio)
boton3.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton3.grid(row=2, column= 2, sticky="e", padx=10, pady=5)  

#Informe
informe = tk.Label(ventana, text="Informe")
informe.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 16, "bold"))
informe.grid(row=4, column=1, padx=45, pady=15, sticky="we") 

#BOTON GENERAR PDF
boton3 = tk.Button(ventana, text="Descargar PDF", width=15, height=1, command=generar_reporte_pdf)
boton3.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton3.grid(row=5, column= 1,padx=45, sticky="w") 

# #BOTON GENERAR JSON
boton4 = tk.Button(ventana, text="Descargar JSON", width=15, height=1, command=generar_reporte_json)
boton4.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton4.grid(row=6, column= 1,padx=45, sticky="w") 

# #BOTON GENERAR XML  
boton5 = tk.Button(ventana, text="Descargar XML", width=15, height=1, command=generar_reporte_xml)
boton5.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton5.grid(row=7, column= 1,padx=45, sticky="w")

ventana.mainloop()
