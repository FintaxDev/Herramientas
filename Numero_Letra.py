def NumeroTexto(numero):

    lstEscalas = [("", ""), ("MIL", "MIL"), ("MILLON", "MILLONES"), ("MIL", "MIL"), ("BILLON", "BILLONES")]
    entero = int(numero)
    decimal = int(round((numero - entero) * 100))
    i = 0
    strNumeroTexto = ""

    while entero > 0:
        a = entero % 1000
        if i == 0:
            strLetras = Convertidor(a, 1)
        else:
            strLetras = Convertidor(a, 0)
        if a == 0:
            strNumeroTexto = strLetras + " " + strNumeroTexto
        elif a == 1:
            if i in (1, 3):
                strNumeroTexto = lstEscalas[i][0] + " " + strNumeroTexto
            else:
                strNumeroTexto = strLetras + " " + lstEscalas[i][0] + " " + strNumeroTexto
        else:
            strNumeroTexto = strLetras + " " + lstEscalas[i][1] + " " + strNumeroTexto

        strNumeroTexto = " ".join(strNumeroTexto.split())
        i = i + 1
        entero = int(entero / 1000)

    strNumeroTexto = "(" + strNumeroTexto + " PESOS " + str(decimal) + "/100 M.N.)"

    return strNumeroTexto.replace("VEINTI ", "VEINTI").replace("(UN PESOS", "(UN PESO")
 
def Convertidor(numero, sw):

    lstEscalasCien = ["", ("CIEN", "CIENTO"), "DOSCIENTOS", "TRESCIENTOS", "CUATROCIENTOS", "QUINIENTOS", "SEISCIENTOS", "SETECIENTOS", "OCHOCIENTOS", "NOVECIENTOS"]

    lstEscalasDiez = ["", ("DIEZ", "ONCE", "DOCE", "TRECE", "CATORCE", "QUINCE", "DIECISEIS", "DIECISIETE", "DIECIOCHO", "DIECINUEVE"), ("VEINTE", "VEINTI"), ("TREINTA", "TREINTA Y"), ("CUARENTA", "CUARENTA Y"), ("CINCUENTA", "CINCUENTA Y"), ("SESENTA", "SESENTA Y"), ("SETENTA", "SETENTA Y"), ("OCHENTA", "OCHENTA Y"), ("NOVENTA", "NOVENTA Y")]

    lstEscalasUno = ["", ("UN", "UN"), "DOS", "TRES", "CUATRO", "CINCO", "SEIS", "SIETE", "OCHO", "NUEVE"]

    centena = int (numero / 100)
    decena = int((numero -(centena * 100)) / 10)
    unidad = int(numero - (centena * 100 + decena * 10))

    texto_centena = ""
    texto_decena = ""
    texto_unidad = ""
 
    texto_centena = lstEscalasCien[centena]
    if centena == 1:
        if (decena + unidad) != 0:
            texto_centena = texto_centena[1]
        else:
            texto_centena = texto_centena[0]
 
    texto_decena = lstEscalasDiez[decena]
    if decena == 1:
        texto_decena = texto_decena[unidad]
    elif decena > 1:
        if unidad != 0:
            texto_decena = texto_decena[1]
        else:
            texto_decena = texto_decena[0]

    if decena != 1:
        texto_unidad = lstEscalasUno[unidad]
        if unidad == 1:
            texto_unidad = texto_unidad[sw]
 
    return "%s %s %s" %(texto_centena, texto_decena, texto_unidad)
