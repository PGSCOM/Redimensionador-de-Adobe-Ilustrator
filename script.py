import os
from pyai import Document

# Definir la ruta de la carpeta donde están los archivos .ai
folder_path = "Ruta a la carpeta de archivos .ai"

# Obtener una lista de todos los archivos .ai en la carpeta anteriormente seleccionada
ai_files = [f for f in os.listdir(folder_path) if f.endswith(".ai")]

# Iterar a través de cada archivo y redimensionarlos
for file_name in ai_files:
    file_path = os.path.join(folder_path, file_name)
    document = Document(file_path)
    document.fit_artboard_to_artwork()
    document.save(file_path)
    print(f"Archivo {file_name} redimensionado correctamente.")