import pytest
from calculadora import evaluar

# Caso 1: orden de operaciones correcto
def test_suma_y_multiplicacion():
    assert evaluar("2 + 3 * 4") == 14

# Caso 2: uso de paréntesis
def test_parentesis():
    assert evaluar("(2 + 3) * 4") == 20

# Caso 3: expresión inválida
def test_expresion_invalida():
    with pytest.raises(ValueError):
        evaluar("2 + * 3")
