# Operadores matemáticos básicos


class Basicos:
    pass

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def suma(self):
        resultado = self.n1 + self.n2
        return resultado

    def resta(self):
        resultado = self.n1 - self.n2
        return resultado

    def multiplicacion(self):
        resultado = self.n1 * self.n2
        return resultado

    def division(self):
        resultado = self.n1 / self.n2
        return resultado
