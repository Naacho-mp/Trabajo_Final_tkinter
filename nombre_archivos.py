from pathlib import Path

ruta = Path('C:/Users/Ignacio/Desktop/plantas')

archivos = [archivo.name for archivo in ruta.iterdir() if archivo.is_file()]

print(archivos)
