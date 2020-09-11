import glob
import sys
from PyPDF2 import PdfFileMerger
from tkinter import *
from tkinter import filedialog, messagebox

root = Tk()
root.withdraw()
root.attributes("-topmost", True)
ubicacion = filedialog.askdirectory(parent=root, initialdir="/", title="Seleccione la carpeta con los archivos a combinar")
if ubicacion == "":
    messagebox.showinfo("Error", "No se ha seleccionado una carpeta.")
else:
    pdfs = []
    for NombreArchivo in sorted(glob.glob(ubicacion + "/*.pdf")):
        pdfs.append(NombreArchivo)
    if not pdfs:
        messagebox.showinfo("Error", "La carpeta seleccionada no contiene archivos PDF.")
    else:
        merger = PdfFileMerger()
        for pdf in pdfs:
            merger.append(pdf)
        merger.write(ubicacion + "/Resultado.pdf")
        merger.close()
        messagebox.showinfo("Terminado", "Se creó el archivo PDF combinado.")
