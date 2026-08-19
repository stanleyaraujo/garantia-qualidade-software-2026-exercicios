from multa import calcular_multa


def test_multa():
    assert calcular_multa(3, 2.0) == 6.0
