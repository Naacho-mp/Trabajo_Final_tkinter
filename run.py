import requests
import json
from pprint import pprint

API_KEY = "2b10UgruUpKmv00I2ZKKWnlo8e"  # Set you API_KEY here
PROJECT = "all" # try "weurope" or "canada"
api_endpoint = f"https://my-api.plantnet.org/v2/identify/{PROJECT}?api-key={API_KEY}&include-related-images=true"


image_path_1 = "C:/Users/Ignacio/Desktop/plantas/planta8.jpg"
image_data_1 = open(image_path_1, 'rb')

data = {
    'organs': ['flower']

}

files = [
    ('images', (image_path_1, image_data_1)),
]

req = requests.Request('POST', url=api_endpoint, files=files, data=data)
prepared = req.prepare()

s = requests.Session()
response = s.send(prepared)
json_result = json.loads(response.text)

pprint(response.status_code)
pprint(json_result)
