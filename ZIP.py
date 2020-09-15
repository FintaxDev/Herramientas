from zipfile import ZipFile

archivo = "Prueba.zip"

carpeta = "Prueba"

with ZipFile(archivo, "r") as zip:
    zip.printdir()
    zip.extractall(carpeta)
