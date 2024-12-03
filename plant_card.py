import tkinter as tk
from PIL import Image, ImageTk

# Clase para crear una tarjeta con la información de la planta
class PlantCard(tk.Frame):
    def __init__(self, parent, planta, **kwargs):
        super().__init__(parent, **kwargs)
        self.planta = planta
        self.create_card()

    def create_card(self):
        # Cargar y redimensionar la imagen
        img = Image.open(self.planta.image_path)
        img.thumbnail((120, 120))  # Ajustamos el tamaño de la imagen para que no sea demasiado grande
        img = ImageTk.PhotoImage(img)

        # Mostrar la imagen
        img_label = tk.Label(self, image=img)
        img_label.image = img  # Necesario para mantener una referencia de la imagen
        img_label.grid(row=0, column=0, rowspan=4, padx=10, pady=10)

        # Crear un marco de texto para el contenido
        text_frame = tk.Frame(self)
        text_frame.grid(row=0, column=1, rowspan=4, sticky="w", padx=10, pady=10)

        # Mostrar el nombre común
        common_name_label = tk.Label(text_frame, text=f"Nombre común: {self.planta.common_name}", font=("Helvetica", 12, "bold"))
        common_name_label.grid(row=0, column=0, sticky="w", pady=5)

        # Mostrar el nombre científico
        scientific_name_label = tk.Label(text_frame, text=f"Nombre científico: {self.planta.scientific_name}", font=("Helvetica", 12))
        scientific_name_label.grid(row=1, column=0, sticky="w", pady=5)

        # Mostrar la familia
        family_label = tk.Label(text_frame, text=f"Familia: {self.planta.family}", font=("Helvetica", 12))
        family_label.grid(row=2, column=0, sticky="w", pady=5)

        # Mostrar el porcentaje de coincidencia
        score_label = tk.Label(text_frame, text=f"Coincidencia: {self.planta.score*100:.2f}%", font=("Helvetica", 12, "italic"))
        score_label.grid(row=3, column=0, sticky="w", pady=5)
