def sum_numbers(a, b):
    a (int, float): El primer número.
    b (int, float): El segundo número.
    
    Retorna:
    int, float: La suma de los dos números.
    return a + b

if __name__ == "__main__":
    # Saludar al usuario
    greet("Mundo")
    
    # Sumar dos números
    num1 = 5
    num2 = 7
    result = sum_numbers(num1, num2)
    print(f"La suma de {num1} y {num2} es {result}")
