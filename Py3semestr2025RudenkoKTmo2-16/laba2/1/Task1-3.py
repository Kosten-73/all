print("5 вариант")
print("3 задача")

r1 = float(input("Введите 1-ое сопротивление R1 = "))    # 1-ое число целое число
r2 = float(input("Введите 2-ое сопротивление R2 = "))    # 2-ое число целое число

print("Цепь подключена последовательно")

round_if_float = lambda sum_r: round(sum_r, 1) if isinstance(sum_r, float) else sum_r

sum_r = round_if_float(r1 + r2)

print(f"Общее сопротивление цепи: {r1} + {r2} = {sum_r} Ом")
