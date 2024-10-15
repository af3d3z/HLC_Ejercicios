def calcular(entrada):
    salida = ""
    if "D" in entrada and "T" in entrada:
        salida = "V"
    elif "T" in entrada and "V" in entrada:
        salida = "D"
    elif "V" in entrada and "D" in entrada:
        salida = "T"

    return salida