from ej2.velocidad import calcular

"""
Tests que ya no funcionan:

def test_velocidad_letras_1():
    assert calcular("D=1 T=1") == "V"
def test_velocidad_letras_2():
    assert calcular("T=1 V=1") == "D"
def test_velocidad_letras_3():
    assert calcular("V=1 D=1") == "T"

def test_velocidad_acceso_numeros_1():
    assert calcular("D=1 T=1") == "V=11"

def test_velocidad_acceso_numeros_2():
    assert calcular("T=1 V=1") == "D=11"

def test_velocidad_acceso_numeros_3():
    assert calcular("V=1 D=1") == "T=11"
"""

def test_velocidad_calculo_1():
    assert calcular("D=32 T=4") == "V=8"

def test_velocidad_calculo_2():
    assert calcular("T=4 V=8") == "D=32"

def test_velocidad_calculo_3():
    assert calcular("V=8 D=32") == "T=4"


def test_velocidad_calculo_cambio_orden_1():
    assert calcular("T=4 D=32") == "V=8"

def test_velocidad_calculo_cambio_orden_2():
    assert calcular("V=8 T=4") == "D=32"

def test_velocidad_calculo_cambio_orden_3():
    assert calcular("D=32 V=8") == "T=4"


def test_velocidad_string_vacio():
    assert calcular("") == ""

def test_velocidad_parametro_incompleto_1():
    assert calcular("D=4") == ""

def test_velocidad_parametro_incompleto_2():
    assert calcular("T=4") == ""

def test_velocidad_parametro_incompleto_3():
    assert calcular("V=4") == ""