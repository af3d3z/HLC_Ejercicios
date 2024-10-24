import re

def calcular(entrada: str):
    salida = ""

    if "D" in entrada and "T" in entrada:
        matches = re.findall(r'([DT])=(\d+)', entrada)
        values = {key: int(value) for key, value in matches}
        salida = "V=" + str(int((values.get('D') / values.get('T'))))
    elif "T" in entrada and "V" in entrada:
        matches = re.findall(r'([T|V])=(\d+)', entrada)
        values = {key: int(value) for key, value in matches}
        salida = "D=" + str(values.get('T') * values.get('V'))
    elif "V" in entrada and "D" in entrada:
        matches = re.findall(r'([DV])=(\d+)', entrada)
        values = {key: int(value) for key, value in matches}
        salida = "T=" + str(int(values.get('D') / values.get('V')))

    return salida
