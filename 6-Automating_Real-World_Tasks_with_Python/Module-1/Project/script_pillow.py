#!/usr/bin/env python3

# Importamos los módulos necesarios
import os  # Para trabajar con el sistema de archivos y rutas
from PIL import Image  # Para procesar imágenes

# Definimos la ruta donde se encuentran las imágenes originales
# Usamos una ruta relativa para facilitar la portabilidad del script
old_path = './images/'  

# Definimos la ruta donde se guardarán las imágenes procesadas
new_path = './icons/'  

# Verificamos si la carpeta de destino existe
# Si no existe, la creamos para evitar errores al guardar los archivos
if not os.path.exists(new_path):
    os.makedirs(new_path)

# Recorremos todos los archivos en el directorio de imágenes originales
for image in os.listdir(old_path):
    # Comprobamos que el archivo no sea oculto (ignorar archivos como '.DS_Store')
    if not image.startswith('.'):
        # Abrimos la imagen utilizando PIL
        img = Image.open(os.path.join(old_path, image))
        
        # Procesamos la imagen:
        # 1. Rotamos la imagen 90 grados en sentido antihorario.
        # 2. Redimensionamos la imagen a 128x128 píxeles.
        # 3. Convertimos la imagen a formato RGB (por si es PNG con transparencia).
        # 4. Guardamos la imagen procesada en el directorio de destino con formato JPEG.
        img.rotate(-90).resize((128, 128)).convert("RGB").save(
            os.path.join(new_path, image.split('.')[0] + '.jpeg'), 'jpeg'
        )
        
        # Cerramos la imagen para liberar recursos del sistema
        img.close()
