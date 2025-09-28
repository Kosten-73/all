import roman

roman_num = input("Введите римское число: ").upper()   # X
arabic_num = int(input("Введите арабское число: "))   # 5

a = roman.fromRoman(roman_num)
b = arabic_num

# Операции
operations = {
    "+": a + b,
    "-": a - b,
    "*": a * b,
    "//": a // b if b != 0 else "деление на ноль"
}

# Выводим результаты
print(f"Римское число {roman_num} = {a}")
print(f"Арабское число = {b}\n")

for op, result in operations.items():
    if isinstance(result, int) and result > 0:  # только положительные можно в римские
        try:
            roman_result = roman.toRoman(result)
        except:
            roman_result = "нельзя перевести"
    else:
        roman_result = "нельзя перевести"
    print(f"{a} {op} {b} = {result}  (римскими: {roman_result})")
