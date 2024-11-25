# Project Problem Statement
You'll need to write a script that processes a bunch of images. It turns out that your company is in the process of updating its website, and a design contractor has been hired to create some new icon graphics for the site. 

However, the contractor has delivered the final designs and they’re in the wrong format, rotated 90° and too large. You’re unable to get in contact with the designers and your own deadline is approaching fast. You’ll need to use Python to get these images ready for launch!

So, how will you do this? You'll need to go through a folder full of images and operate with each of them. On each image, you'll use PIL methods like the ones we saw in the examples, and then write the new images in the right place.

## What you’ll do
Use the Python Imaging Library to do the following to a batch of images:

- Open an image

- Rotate an image

- Resize an image

- Save an image in a specific format in a separate directory 


# Curl para la descarga de los archivos

```bash
curl -c ./cookie -s -L "https://drive.google.com/uc?export=download&id=$11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" > /dev/null | curl -Lb ./cookie "https://drive.google.com/uc?export=download&confirm=`awk '/download/ {print $NF}' ./cookie`&id=11hg55-dKdHN63yJP20dMLAgPJ5oiTOHF" -o images.zip && sudo rm -rf cookie
```

# Descomprimir los archivos

```bash
unzip images.zip
```


## Script

- Permisos
    ```bash
    chmod +x <script_name>.py
    ```

- [Código del script](/6-Automating_Real-World_Tasks_with_Python/Module-1/Project/script_pillow.py)

    ```python
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
    ```