def is_palindrome_in_base(n, base):
    # Функция для проверки, является ли число n палиндромом в системе счисления base
    n_str = str(n)
    converted_str = base_conversion(n_str, 10, base)
    return converted_str == converted_str[::-1]

def base_conversion(number, from_base, to_base):
    # Функция для конвертации числа из одной системы счисления в другую
    return "{0}".format(int(number, from_base)).lstrip("0") if number != "0" else "0"

def is_prime(num):
    # Функция для проверки, является ли число простым
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

count_palindromes_primes = 0
upper_limit = 1000000
base = 7

print("Седьмичные палиндромы, являющиеся простыми числами:")
for i in range(upper_limit):
    if is_palindrome_in_base(i, base) and is_prime(i):
        print(base_conversion(str(i), 10, base))
        count_palindromes_primes += 1

print(f"\nКоличество седьмичных палиндромов, являющихся простыми числами, до {upper_limit}: {count_palindromes_primes}")
