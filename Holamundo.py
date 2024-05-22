print ("Anggy")
number = 4

#  Variables
a = 10
b = 14

# Operaciones 
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

# Resultados
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# funcion de un saludo a walter
def saludar_a_walter():
    return "¡Hola Walter! ¿Cómo estás?"

saludo = saludar_a_walter()
print(saludo)


# Condicional
def comparar(a, b):
    if a < b:
        return "a es menor que b"
    elif a > b:
        return "a es mayor que b"
    else:
        return "a es igual a b"

# Ejemplo de uso de la función
a = 5
b = 3

resultado = comparar(a, b)
print(resultado)
