'Definir variables
NombreCarpeta = "Mi Carpeta"
ArchivoExcel = "Excel.xlsx"
ArchivoWord = "Word.docx"

'Ruta de la carpeta a crear
Ruta = "C:\Users\--------\Desktop"

'Crear la carpeta
Set objCarpeta = CreateObject("Scripting.FileSystemObject")
objCarpeta.CreateFolder Ruta & "\" & NombreCarpeta

'Crear el archivo de Excel
Set objExcel = CreateObject("Excel.Application")
Set objWorkbooks = objExcel.workbooks.add()

'Agregar texto (Fila, Columna)
objExcel.cells(1, 1).value = "Hola"
objExcel.cells(1, 2).value = "Mundo!"

'Guardar y cerrar
objWorkbooks.SaveAs(Ruta & "\" & NombreCarpeta & "\" & ArchivoExcel)
objWorkbooks.Close
objExcel.Quit

'Crear el archivo de Word
Set objWord = CreateObject("Word.Application")
Set objDocuments = objWord.Documents.Add()
Set objSelection = objWord.Selection

'Agregar texto al documento
objSelection.Font.Name = "Arial"
objSelection.Font.Size = "11"
objSelection.TypeText "Hola Mundo!"

'Guardar y cerrar
objDocuments.SaveAs(Ruta & "\" & NombreCarpeta & "\" & ArchivoWord)
objDocuments.Close
objWord.Quit

'Crear cuadro de mensaje
MsgBox "La carpeta y los archivos fueron creados", ,"Terminado"