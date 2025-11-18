import numpy as np

# Variant 2: Matrix operations (3x3)
# Создание матриц A и B
a = np.random.randint(1, 10, (3, 3))  # случайные числа 1-9
b = np.random.randint(1, 10, (3, 3))

# Сумма
sum_ab = a + b

# Разница
sub_ab = a - b

# Матричное умножение
mul_ab = a @ b

# Логическая матрица совпадений
matches = a == b

# Вывод результатов
print("Матрица A:\n", a)
print("\nМатрица B:\n", b)
print("\nA + B =\n", sum_ab)
print("\nA - B =\n", sub_ab)
print("\nA @ B =\n", mul_ab)
print("\nСовпадающие элементы (True = совпадает):\n", matches)
