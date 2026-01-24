import roman

roman_x = input("Введите римское число: ").upper()   # X
roman_y = input("Введите римское число: ").upper()   # X

x = roman.fromRoman(roman_x)
y = roman.fromRoman(roman_y)
# Операции
operations = {
    "+": x + y,
}

# Выводим результаты
print(f"Римское число 1 {roman_x}")
print(f"Римское число 2 {roman_y}")

for op, result in operations.items():
    if isinstance(result, int) and result > 0:
        try:
            roman_result = roman.toRoman(result)
        except:
            roman_result = "нельзя перевести"
    else:
        roman_result = "нельзя перевести"
    print(f"{a} {op} {b} = {result}  (римскими: {roman_result})")
