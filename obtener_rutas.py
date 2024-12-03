from pathlib import Path

def obtener_rutas_imagenes(ruta_directorio):
    ruta_directorio = Path(ruta_directorio)
    nombres_archivos = [archivo.name for archivo in ruta_directorio.iterdir() if archivo.is_file()]   

    nombres_imagenes = []
    for i in nombres_archivos:
        if i.endswith(('.jpg', '.png')):
            nombres_imagenes.append(i)

    rutas_imagenes = []
    for i in nombres_imagenes:
        rutas_imagenes.append(ruta_directorio / i)

    #convertir rutas a str
    rutas_imagenes = [str(ruta) for ruta in rutas_imagenes]

    return rutas_imagenes


print(obtener_rutas_imagenes("C:/Users/nicol/Desktop/5519240445_8746faf3f0_z.jpg"))