import tkinter as tk
from PIL import Image, ImageTk

class Planta:
    def __init__(self, common_name, scientific_name, family, score, image_path):
        self.common_name = common_name
        self.scientific_name = scientific_name
        self.family = family
        self.score = score
        self.image_path = image_path
    
    def pasar_a_lista(self):
        return[self.common_name, self.scientific_name, self.family, self.score, self.image_path]


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

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Tarjeta de Planta")

    planta = Planta(
        common_name="Chilean-bellflower",
        scientific_name="Lapageria rosea Ruiz & Pav.",
        family="Philesiaceae",
        score=0.80134,
        image_path="planta6.jpg"  # Cambia esto a la ruta de tu imagen
    )

    plant_card = PlantCard(root, planta)
    plant_card.pack(padx=20, pady=20)

    root.mainloop()
