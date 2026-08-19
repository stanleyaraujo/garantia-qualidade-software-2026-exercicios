from multa import calcular_multa


def test_sem_atraso():
    assert calcular_multa(0, 2.0) == 0.0


def test_atraso_positivo():
    assert calcular_multa(3, 2.0) == 6.0


def test_atraso_negativo():
    assert calcular_multa(-2, 2.0) == 0.0


def test_valor_diario_fracionario():
    assert calcular_multa(3, 2.5) == 7.5
