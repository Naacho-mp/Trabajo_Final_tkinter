import tkinter as tk

#edicion

ventana = tk.Tk() # Acá tenemos nuestro objeto ventana. Es propio del paquete.␣

ventana.title("Plant Review") # Este es un método
ventana.geometry("600x600") # Dimensiones
ventana.minsize(100, 100)
ventana.maxsize(1280, 720)
ventana.iconbitmap("icono_plant.ico") # Agregar un icono
ventana.configure(bg="White")

ventana.geometry("600x600+100+8") # Podemos agregar las coordenadas
ventana.attributes("-alpha", 1.0) # Controlar la opacidad
ventana.resizable(True, True) #Bloque de la ventana 

def cambiar_color():
    ventana.config(bg="chartreuse2")

#ETIQUETAS
titulo = tk.Label(ventana, text="🌱 Plant Review 🍂")
titulo.config(fg="black", bg="OliveDrab1", anchor= "w", font=("Times New Roman", 16, "bold"))
titulo.grid(row=0, column=0, padx=20, pady=15, sticky="w")  

sub_titulo = tk.Label(ventana, text="Sube tu imagen (planta, arbusto, hierba o flor)")
sub_titulo.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 12, "bold"))
sub_titulo.grid(row=1, column=0, padx=25, pady=15, sticky="w")  

#FRAME 
frame1 = tk.Frame(ventana) 
frame1.configure(width=430, height=90, bg='gray85')
frame1.grid(row=2, column=0, padx=30, pady=5) 

#BOTON
boton = tk.Button(ventana, text="Subir ⬆", width=10, height=1)
boton.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10))
boton.grid(row=2, column= 0)

#Resultados titulo
resultados = tk.Label(ventana, text="Resultados - Análisis")
resultados.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 14, "bold"))
resultados.grid(row=4, column=0, padx=25, pady=5, sticky="w") 

#BOTON 2
boton2 = tk.Button(ventana, text="Analizar 🔎", width=10, height=1)
boton2.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton2.grid(row=3, column= 0, sticky="w", padx=300)


#Resultados Imagen
resul_img = tk.Label(ventana, text="Imagen ")
resul_img.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 12))
resul_img.grid(row=5, column=0, padx=25, sticky="w") 

#FRAME IMAGEN
frame_imagen = tk.Frame(ventana) 
frame_imagen.configure(width=350, height=200, bg='gray85')
frame_imagen.grid(row=6, column=0, padx=150, pady=15)


#Resultados Nombre
resul_name = tk.Label(ventana, text="Nombre: ")
resul_name.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 12))
resul_name.grid(row=7, column=0, padx=25,pady=5, sticky="w") 

#Resultados Nombre cientifico
resul_name_cient = tk.Label(ventana, text="Nombre Cientifico ")
resul_name_cient.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 12))
resul_name_cient.grid(row=8, column=0, padx=25,pady=5, sticky="w") 

#Resultados Descripcion
resul_descripcion = tk.Label(ventana, text="Descripción ")
resul_descripcion.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 12))
resul_descripcion.grid(row=9, column=0, padx=25, pady=5,sticky="w") 

#TITULO 2
titulo_2 = tk.Label(ventana, text="Analizar Directorio")
titulo_2.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 14, "bold"))
titulo_2.grid(row=0, column=1, padx=45, pady=5, sticky="we")  

#SUBTITULO DIRECTORIO
sub_titulo_2 = tk.Label(ventana, text="Ruta del Directorio")
sub_titulo_2.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 12))
sub_titulo_2.grid(row=1, column=1, padx=45, pady=5, sticky="w")  
#ENTRADA
entrada = tk.Entry(ventana)
entrada.config(fg = "black", bg="gray85", font=("Arial", 12))
entrada.grid(row=2, column=1, padx=45, sticky="e")

#BOTON 3
boton3 = tk.Button(ventana, text="Analizar Directorio", width=15, height=1)
boton3.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton3.grid(row=2, column= 2, sticky="e", padx=10, pady=5)  

#Informe
informe = tk.Label(ventana, text="Informe")
informe.config(fg="black", bg="white", anchor= "w", font=("Times New Roman", 14, "bold"))
informe.grid(row=4, column=1, padx=45, pady=15, sticky="we") 

#BOTON 4
boton3 = tk.Button(ventana, text="Descargar PDF", width=15, height=1)
boton3.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10,"bold"))
boton3.grid(row=5, column= 1,padx=45, sticky="w") 


#INSERTAR IMAGEN
# imagen = tk.PhotoImage(file="icono_plant.ico")
# label_imagen = tk.Label(ventana, image=imagen)
# label_imagen.pack()

ventana.mainloop()