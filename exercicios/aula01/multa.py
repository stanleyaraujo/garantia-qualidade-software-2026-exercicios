def calcular_multa(dias_atraso: int, valor_diario: float) -> float:
    """Multa por atraso na devolução. Sem atraso, soma 0."""
    if dias_atraso <= 0:
        return 0.0
    return dias_atraso * valor_diario
