# Задача 1

def draw_frame(s, k):
    """
    Рисует рамку из символа k вокруг строки s

    Args:
        s (str): строка для обрамления
        k (str): символ для рамки
    """
    if len(k) != 1:
        raise ValueError(f"Символ рамки должен быть длиной 1, получено: '{k}' (длина: {len(k)})")
    # Верхняя и нижняя линии рамки - длина строки + 2 символа по бокам
    top_bottom = k * (len(s) + 2)

    # Средняя линия с текстом
    middle = f"{k}{s}{k}"

    # Вывод рамки
    print(top_bottom)
    print(middle)
    print(top_bottom)

try:
    s = input("Введите строку которая будет выведена в рамке \"s\": ")
    k = input("Введите символ для рамки \"k\": ")
    draw_frame(s, k)
except ValueError as e:
    print(f"Ошибка: {e}")
except Exception as e:
    print(f"Произошла непредвиденная ошибка: {e}")

# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba3\Task3-1.py
# Введите строку которая будет выведена в рамке "s": Текст в рамке
# Введите символ для рамки "k": *
# ***************
# *Текст в рамке*
# ***************
#
# Process finished with exit code 0


# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba3\Task3-1.py
# Введите строку которая будет выведена в рамке "s": Хочу получить баллов за лабу
# Введите символ для рамки "k": 6
# 666666666666666666666666666666
# 6Хочу получить баллов за лабу6
# 666666666666666666666666666666
#
# Process finished with exit code 0


# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba3\Task3-1.py
# Введите строку которая будет выведена в рамке "s": Тест
# Введите символ для рамки "k": плохой
# Ошибка: Символ рамки должен быть длиной 1, получено: 'плохой' (длина: 6)
#
# Process finished with exit code 0
