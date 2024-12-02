import tkinter as tk

ventana = tk.Tk() # Acá tenemos nuestro objeto ventana. Es propio del paquete.␣

ventana.title("Plant Review") # Este es un método
ventana.geometry("600x600") # Dimensiones
ventana.minsize(100, 100)
ventana.maxsize(1920, 1080)
ventana.iconbitmap("icono_plant.ico") # Agregar un icono
ventana.configure(bg="White")

ventana.geometry("600x600+100+8") # Podemos agregar las coordenadas
ventana.attributes("-alpha", 1.0) # Controlar la opacidad
ventana.resizable(True, True) #Bloque de la ventana 

#ETIQUETAS TITULO 
titulo = tk.Label(ventana, text="🌱 Plant Review")
titulo.config(fg="black", bg="OliveDrab1", anchor="w", font=("Times New Roman", 16, "bold"))
titulo.pack(padx=20, pady=5, anchor="w")

#TITULO - ANALISIS DIRECTORIO
titulo_2 = tk.Label(ventana, text="Analizar Directorio")
titulo_2.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 14, "bold"))
titulo_2.pack(padx=485, anchor="e")

#SUBTITULO ANALISIS - DIRECTORIO
sub_titulo_2 = tk.Label(ventana, text="Ruta del Directorio")
sub_titulo_2.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 12 ))
sub_titulo_2.pack(padx=485, anchor="e")

#SUBTITULO
sub_titulo = tk.Label(ventana, text="Sube tu imagen (planta, arbusto, hierba o flor)")
sub_titulo.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 12, "bold"))
sub_titulo.pack(padx=25, pady=5, anchor="w")

#FRAME 
frame1 = tk.Frame(ventana) 
frame1.configure(width=480, height=120, bg='gray85')
frame1.pack(padx=30, pady=5, anchor="w")

#BOTON 1
boton = tk.Button(frame1, text="Subir ⬆", width=10, height=1)
boton.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10))
boton.pack(padx=250, pady= 50, anchor="w")

#BOTON 2
boton2 = tk.Button(ventana, text="Analizar", width=10, height=1)
boton2.config(fg="black", bg="OliveDrab1", font=("Times New Roman", 10))
boton2.pack(pady=5, anchor="w", padx=530)

#Resultados titulo
resultados = tk.Label(ventana, text="Resultados - Análisis")
resultados.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 14, "bold"))
resultados.pack(padx=25, pady=5, anchor="w")

#Resultados Imagen
resul_img = tk.Label(ventana, text="Imagen ")
resul_img.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 12))
resul_img.pack(padx=25, pady=5, anchor="w")

#FRAME IMAGEN - RESULTADO
frame_img = tk.Frame(ventana) 
frame_img.configure(width=350, height=200, bg='gray85')
frame_img.pack(padx=150, pady=5, anchor="w")

#Resultados Nombre
resul_name = tk.Label(ventana, text="Nombre: ")
resul_name.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 12))
resul_name.pack(padx=25, pady=5, anchor="w")

#Resultados Nombre cientifico
resul_name_cient = tk.Label(ventana, text="Nombre Cientifico ")
resul_name_cient.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 12))
resul_name_cient.pack(padx=25, pady=5, anchor="w")

#Resultados Descripcion
resul_descripcion = tk.Label(ventana, text="Descripción ")
resul_descripcion.config(fg="black", bg="white", anchor="w", font=("Times New Roman", 12))
resul_descripcion.pack(padx=25, pady=5, anchor="w")

#INSERTAR IMAGEN
# imagen = tk.PhotoImage(file="icono_plant.ico")
# label_imagen = tk.Label(ventana, image=imagen)
# label_imagen.pack()

ventana.mainloop()
