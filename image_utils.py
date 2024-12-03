import requests
import json
from tkinter import filedialog
from planta import Planta
from nombre_archivos import obtener_rutas_imagenes

def cargar_imagen():
    image_path = filedialog.askopenfilename(filetypes=[("Imagenes", "*.jpg;*.jpeg;*.png")])
    return image_path

API_KEY = "2b10UgruUpKmv00I2ZKKWnlo8e"
PROJECT = "all"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}&include-related-images=true"

def analizar_imagen(image_path):
    if not image_path:
        print("No se ha cargado ninguna imagen.")
        return None

    image_data = open(image_path, 'rb')
    data = {'organs': ['flower']}
    files = [('images', (image_path, image_data))]

    req = requests.Request('POST', url=api_endpoint, files=files, data=data)
    prepared = req.prepare()

    s = requests.Session()
    response = s.send(prepared)

    if response.status_code == 200:
        json_result = json.loads(response.text)
        
        if 'results' in json_result and len(json_result['results']) > 0:
            best_match = json_result['results'][0]
            species_name = best_match['species']['scientificNameWithoutAuthor']
            common_name = best_match['species'].get('commonNames', ['Sin nombre común'])[0]
            family = best_match['species'].get('family', 'Desconocida')
            family = family.get('scientificNameWithoutAuthor', 'Desconocida')
            score = best_match.get('score', 0)

            planta = Planta(common_name, species_name, family, score, image_path)
            return planta
        else:
            print("No se encontraron resultados.")
            return None
    else:
        print(f"Error en la solicitud: {response.status_code}")
        return None


def obtener_plantas_por_directorio(ruta_directorio):
    rutas_imagenes = obtener_rutas_imagenes(ruta_directorio)

    plantas = []
    for ruta_imagen in rutas_imagenes:
        planta = analizar_imagen(ruta_imagen)
        if planta:
            plantas.append(planta)

    for planta in plantas:
        print(f"Nombre común: {planta.common_name}")
        print(f"Nombre Cientifico: {planta.scientific_name}")
        print(f"Descripción: {planta.family}")
        print(f"Puntuación: {planta.score}")
        print(f"Ruta de la imagen: {planta.image_path}")

    return plantas
