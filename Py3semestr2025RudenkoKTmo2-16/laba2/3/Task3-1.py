# Задача 1
a = int(input("Введите высоту форточки (a, см): "))
b = int(input("Введите ширину форточки (b, см): "))
d = int(input("Введите диаметр головы Васи (d, см): "))
if d <= a - 2 and d <= b - 2:
    print("Вася прирожденный форточник!)")
else:
    print("Васе прийдется устроиться на работу - он в форточку не пролез")

# Или
if d <= min(a - 2, b - 2):
    print("Вася прирожденный форточник!)")
else:
    print("Васе прийдется устроиться на работу - он в форточку не пролез")

# C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\.venv\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba2\3\Task3-1.py
# Введите высоту форточки (a, см): 12
# Введите ширину форточки (b, см): 20
# Введите диаметр головы Васи (d, см): 10
# Вася прирожденный форточник!)
# Вася прирожденный форточник!)
#
# Process finished with exit code 0
