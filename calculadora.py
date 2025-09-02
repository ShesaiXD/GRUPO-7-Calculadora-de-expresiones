def evaluar(expresion: str) -> float:
    try:
        # Solo permitimos números, espacios, paréntesis y operadores básicos
        permitido = "0123456789+-*/(). "
        if any(c not in permitido for c in expresion):
            raise ValueError("Expresión no válida")

        # Usamos eval porque respeta orden de operaciones y paréntesis
        return eval(expresion)
    except Exception:
        # Si hay un error de sintaxis o similar
        raise ValueError("Expresión inválida")
