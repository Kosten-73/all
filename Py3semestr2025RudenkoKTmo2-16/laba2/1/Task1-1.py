print("5 вариант")
print("1 задача")

x = int(input("Введите 1-ое целое число x = "))    # 1-ое число целое число
y = int(input("Введите 2-ое целое число y = "))    # 2-ое число целое число

# лямбда выражение которое проверяет вещественое ли число ? в случае True округляет до 2 знаков после запятой
round_if_float = lambda now: round(now, 2) if isinstance(now, float) else now

# Арифметические операции
# +, -, *, /, //, %, **
print("Арифметические операции")
print("+, -, *, /, //, %, **")
# +
print(f"{x} + {y} = {x + y}")
# -
print(f"{x} - {y} = {x - y}")
print(f"{y} - {x} = {y - x}")
# *
print(f"{x} * {y} = {x * y}")
# /
print(f"{x} / {y} = {round_if_float(x / y)}")
print(f"{y} / {x} = {round_if_float(y / x)}")
# //
print(f"{x} // {y} = {x // y}")
print(f"{y} // {x} = {y // x}")
# %
print(f"{x} % {y} = {x % y}")
print(f"{y} % {x} = {y % x}")
# **
print(f"{x}**{y} = {x**y}")
print(f"{y}**{x} = {y**x}")

# Операции сравнения
# <, <=, >, >=, !=, ==
print("Операции сравнения")
print("<, <=, >, >=, !=, ==")
# <
print(f"{x} < {y} = {x < y}")
print(f"{y} < {x} = {y < x}")
# <=
print(f"{x} <= {y} = {x <= y}")
print(f"{y} <= {x} = {y <= x}")
# >
print(f"{x} > {y} = {x > y}")
print(f"{y} > {x} = {y > x}")
# >=
print(f"{x} >= {y} = {x >= y}")
print(f"{y} >= {x} = {y >= x}")
# !=
print(f"{x} != {y} = {x != y}")
# ==
print(f"{x} == {y} = {x == y}")
