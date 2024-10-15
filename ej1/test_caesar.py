from ej1.caesar import encode


def test_caesar():
    assert encode("a", 1) == "b"
    assert encode("a", 5) == "f"
    assert encode("z", 4) == "d"
    assert encode("ab", 2) == "cd"
    assert encode("hola", 6) == "nuqg"
    assert encode("sa h", 4) == "we l"
    assert encode("mañanas", 32) == "qfsfrfx"