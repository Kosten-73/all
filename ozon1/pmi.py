import numpy as np
from scipy.interpolate import lagrange

# Заданные значения функции
x_values = [0, 1, 2, 3]
y_values = [-1, 2, 1, 8]

# Построение интерполяционного многочлена Лагранжа
poly = lagrange(x_values, y_values)

# Определение значения функции при x = 0.1 с помощью интерполяционного многочлена
result_at_x_0_1 = poly(0.1)
result_at_x_0_11 = poly(1.5)
print(result_at_x_0_11)
print("Значение функции при x = 0.1:", result_at_x_0_1)
