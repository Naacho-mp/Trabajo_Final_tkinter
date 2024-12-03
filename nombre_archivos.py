from pathlib import Path

ruta = Path('C:/Users/Ignacio/Desktop/plantas')

archivos = [archivo.name for archivo in ruta.iterdir()
            if archivo.is_file()]

solo_img = []

for i in archivos:
    if i.endswith(('.jpg', '.png')):
        solo_img.append(i)

print(solo_img)
