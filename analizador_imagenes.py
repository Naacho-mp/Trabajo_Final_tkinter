import requests
import json
from planta import Planta
from pathlib import Path

class AnalizadorPlantas:
    API_KEY = "2b10UgruUpKmv00I2ZKKWnlo8e"
    PROJECT = "all"
    api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}&include-related-images=true"

    def __init__(self):
        pass

    def obtener_rutas_imagenes(self, ruta_directorio):
        ruta_directorio = Path(ruta_directorio)
        nombres_imagenes = [archivo.name for archivo in ruta_directorio.iterdir() if archivo.is_file() and archivo.name.endswith(('.jpg', '.png'))]
        return [str(ruta_directorio / i) for i in nombres_imagenes]
    

    def analizar_imagen(self, image_path):
        """
        Analiza la imagen usando la API de PlantNet y devuelve una instancia de Planta con los datos.
        """
        if not image_path:
            print("No se ha cargado ninguna imagen.")
            return None

        try:
            with open(image_path, 'rb') as image_data:
                data = {'organs': ['flower']}
                files = [('images', (image_path, image_data))]

                req = requests.Request('POST', url=self.api_endpoint, files=files, data=data)
                prepared = req.prepare()
                s = requests.Session()
                response = s.send(prepared)

                if response.status_code == 200:
                    try:
                        json_result = json.loads(response.text)
                        if 'results' in json_result and len(json_result['results']) > 0:
                            best_match = json_result['results'][0]
                            species_name = best_match['species']['scientificNameWithoutAuthor']
                            common_name = best_match['species'].get('commonNames', ['Sin nombre común'])[0]
                            family = best_match['species'].get('family', 'Desconocida')
                            family = family.get('scientificNameWithoutAuthor', 'Desconocida')
                            score = best_match.get('score', 0)
                            return Planta(common_name, species_name, family, score, image_path)
                    except json.JSONDecodeError:
                        print("Error al procesar el JSON.")
                else:
                    print(f"Error en la solicitud: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error en la solicitud HTTP: {e}")
        return None

    def obtener_plantas_por_directorio(self, ruta_directorio):
        """
        Obtiene las imágenes del directorio especificado y devuelve una lista de instancias de Planta.
        """
        rutas_imagenes = self.obtener_rutas_imagenes(ruta_directorio)
        plantas = []
        for ruta_imagen in rutas_imagenes:
            planta = self.analizar_imagen(ruta_imagen)
            if planta:
                plantas.append(planta)
        return plantas
