# Código principal de la calculadora
# Importamos a los operadores básicos del paquete de operadores, en el se pueden agregar más módulos
# de operaciones más avanzadas
from operadores.basicos import *

print("Calculadora Básica V.1.0")

# Se inicializan primero las variables de los datos numéricos (Por buena práctica, para que el IDE no tenga el error
# de que las variables no se puedan definir)
numero1 = ""
numero2 = ""

# Se ingresan los datos a operar con sus excepciones
while True:
    try:
        numero1 = float(input("Primer Número: "))
    except ValueError:
        print('\n' "Por favor ingrese solo números")
        continue
    else:
        break

while True:
    operador = input("Seleccione la operación matemática: ")

    if operador == '+':
        break
    elif operador == '-':
        break
    elif operador == '*':
        break
    elif operador == '/':
        break
    else:
        print('\n' "La operación es incorrecta")

while True:
    try:
        numero2 = float(input("Segundo Número: "))
    except ValueError:
        print('\n' "Por favor ingrese solo números")
        continue
    else:
        break


# Clase principal Calculadora
class Calculadora:
    pass

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    @staticmethod
    def tipo_operacion():
        if operador == '+':
            resultado = op_basicos.suma()
            return f"El resultado es {resultado}"
        elif operador == '-':
            resultado = op_basicos.resta()
            return f"El resultado es {resultado}"
        elif operador == '*':
            resultado = op_basicos.multiplicacion()
            return f"El resultado es {resultado}"
        elif operador == '/':
            resultado = op_basicos.division()
            return f"El resultado es {resultado}"


# Se instancia el módulo basicos.py
op_basicos = Basicos(numero1, numero2)

# Se instancia la clase Calculadora para poder operar los datos ingresados
calculadora = Calculadora(numero1, numero2)

# Se inicializa el método tipo_operacion() para realizar las operaciones
print(calculadora.tipo_operacion())
