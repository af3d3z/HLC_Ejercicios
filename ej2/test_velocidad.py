from ej2.velocidad import calcular


def test_velocidad_letras():
    assert calcular("D=1 T=1") == "V"
    assert calcular("T=1 V=1") == "D"
    assert calcular("V=1 D=1") == "T"

