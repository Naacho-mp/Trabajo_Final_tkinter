import requests
import json
from planta import Planta
from nombre_archivos import obtener_rutas_imagenes

class AnalizadorPlantas:
    API_KEY = "2b10UgruUpKmv00I2ZKKWnlo8e"
    PROJECT = "all"
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}&include-related-images=true"

    def __init__(self):
        pass

    def analizar_imagen(self, image_path):
        """
        Analiza la imagen usando la API de PlantNet y devuelve una instancia de Planta con los datos.
        """
        if not image_path:
            print("No se ha cargado ninguna imagen.")
            return None

        # Abrir la imagen y preparar la solicitud
        with open(image_path, 'rb') as image_data:
            data = {'organs': ['flower']}
            files = [('images', (image_path, image_data))]

            req = requests.Request('POST', url=self.api_endpoint, files=files, data=data)
            prepared = req.prepare()

            s = requests.Session()
            response = s.send(prepared)

            # Si la respuesta es exitosa, procesamos el JSON
            if response.status_code == 200:
                json_result = json.loads(response.text)

                if 'results' in json_result and len(json_result['results']) > 0:
                    best_match = json_result['results'][0]
                    species_name = best_match['species']['scientificNameWithoutAuthor']
                    common_name = best_match['species'].get('commonNames', ['Sin nombre común'])[0]
                    family = best_match['species'].get('family', 'Desconocida')
                    family = family.get('scientificNameWithoutAuthor', 'Desconocida')
                    score = best_match.get('score', 0)

                    # Crear un objeto Planta con los datos obtenidos
                    planta = Planta(common_name, species_name, family, score, image_path)
                    return planta
                else:
                    print("No se encontraron resultados.")
                    return None
            else:
                print(f"Error en la solicitud: {response.status_code}")
                return None

    def obtener_plantas_por_directorio(self, ruta_directorio):
        """
        Obtiene las imágenes del directorio especificado y devuelve una lista de instancias de Planta.
        """
        # Obtener las rutas de las imágenes desde la función proporcionada
        rutas_imagenes = obtener_rutas_imagenes(ruta_directorio)

        plantas = []
        for ruta_imagen in rutas_imagenes:
            planta = self.analizar_imagen(ruta_imagen)
            if planta:
                plantas.append(planta)

        # Imprimir los resultados de las plantas encontradas
        for planta in plantas:
            print(f"Nombre común: {planta.common_name}")
            print(f"Nombre Cientifico: {planta.scientific_name}")
            print(f"Descripción: {planta.family}")
            print(f"Puntuación: {planta.score}")
            print(f"Ruta de la imagen: {planta.image_path}")

        return plantas
