from PIL import Image
import os

# definir la ruta a la carpeta con las imágenes
ruta_imagenes = 'C:/Users/xeon-2690/Downloads/Skins/mobile'

# definir el tamaño y la calidad deseados
calidad = 30

# recorrer todas las imágenes en la carpeta
for nombre_archivo in os.listdir(ruta_imagenes):
    # verificar que el archivo sea una imagen
    if nombre_archivo.endswith('.jpg') or nombre_archivo.endswith('.png'):
        # abrir la imagen
        imagen = Image.open(os.path.join(ruta_imagenes, nombre_archivo))  
        
         # obtener el nombre y la extensión del archivo
        nombre, extension = os.path.splitext(nombre_archivo)
        
        # agregar "_mini" al nombre del archivo
        nombre_nuevo = nombre + '_preview' + extension
        
        # guardar la imagen con la nueva calidad
        ruta_nuevo = os.path.join(ruta_imagenes, nombre_nuevo)
        imagen.save(ruta_nuevo, optimize=True, quality=calidad)
