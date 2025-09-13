# Задача 1
a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b: "))
# Пункт 1
print("Числа от минимального до максимального:")
for i in range(min(a, b), max(a, b) + 1):
    print(i, end=' ')
# Пункт 2
print("\nЧисла от максимального до минимального столбиком:")
for i in range(max(a, b), min(a, b) - 1, - 1):
    print(i)

# C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\.venv\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba2\3\Task3-6.py
# Введите целое число a: 3
# Введите целое число b: 7
# Числа от минимального до максимального:
# 3 4 5 6 7
# Числа от максимального до минимального столбиком:
# 7
# 6
# 5
# 4
# 3
#
# Process finished with exit code 0
