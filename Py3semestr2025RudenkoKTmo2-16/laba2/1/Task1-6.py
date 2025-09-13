print("5 вариант")
print("6 задача")

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))

# Ввод границ отрезка
m = int(input("Введите левую границу отрезка m: "))
n = int(input("Введите правую границу отрезка n: "))

round_if_float = lambda x: round(x, 1) if isinstance(x, float) else x
print("Нахождение корня уравнения")
if m <= n:
    if a == 0:
        if b == 0:
            print("Уравнение имеет бесконечно много решений")
        else:
            print("Уравнение не имеет решений")
    else:
        x = round_if_float(-b / a)
        in_interval = m <= x <= n

        print(f"Решение уравнения {a} * x + {b} = 0 \n"
              f"Ответ x = {x}")
        print(f"Попадает ли {x} в отрезок: [{m}; {n}]? {'✓ Да' if in_interval else '✗ Нет'}!")
else:
    print("Левая граница отрезка не может быть больше правой")
