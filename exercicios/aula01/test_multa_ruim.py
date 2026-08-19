from multa import calcular_multa


def test_multa():
    assert calcular_multa(3, 2.0) == 6.0


def test_sem_atraso():
    assert calcular_multa(0, 2.0) == 0.0
