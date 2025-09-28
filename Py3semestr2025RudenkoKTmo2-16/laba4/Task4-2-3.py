import math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    return abs(a * b) // gcd(a, b) if a != 0 and b != 0 else 0

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def reciprocal(n):
    if n == 0:
        raise ZeroDivisionError("Невозможно найти обратное число к нулю")
    return 1 / n

def square_root(n):
    if n < 0:
        raise ValueError("Невозможно извлечь корень из отрицательного числа")
    return math.sqrt(n)


def gcd_multiple(*numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result


def lcm_multiple(*numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = lcm(result, num)
    return result

if __name__ == "__main__":
    print("Тестирование модуля numbers.py:")
    print(f"НОД(12, 18) = {gcd(12, 18)}")
    print(f"НОК(12, 18) = {lcm(12, 18)}")
    print(f"Простое число 17: {is_prime(17)}")
    print(f"Простое число 15: {is_prime(15)}")
    print(f"Обратное число к 4: {reciprocal(4)}")
    print(f"Корень из 16: {square_root(16)}")

    print(f"\nНОД(24, 36, 48) = {gcd_multiple(24, 36, 48, 60)}")
    print(f"НОК(3, 4, 6) = {lcm_multiple(3, 4, 6)}")
