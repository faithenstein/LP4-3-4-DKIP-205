# Лабораторная работа №4: Изучение интегрированной среды разработчика
# Выполняли Бахтин Данила, Бритвин Антон
# ДКИП-205
# Вариант 3-4

def print_hex_multiplication_table(n):
    print("Hex Multiplication Table (up to {0} x {0}):".format(n))
    for i in range(1, n+1):
        for j in range(1, n+1):
            result = hex(i * j)[2:].upper()  # Получаем результат умножения и конвертируем в шестнадцатеричное число
            print(f"{hex(i)[2:]} x {hex(j)[2:]} = {result}")

def print_hex_addition_table(n):
    print("Hex Addition Table (up to {0} + {0}):".format(n))
    for i in range(1, n+1):
        for j in range(1, n+1):
            result = hex(i + j)[2:].upper()  # Получаем результат сложения и конвертируем в шестнадцатеричное число
            print(f"{hex(i)[2:]} + {hex(j)[2:]} = {result}")

n = 16  # Максимальное число для таблицы
print_hex_multiplication_table(n)
print()
print_hex_addition_table(n)