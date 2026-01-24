class Roman:
    _values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    def __init__(self, roman_str):
        self.roman = roman_str.upper()

    def _to_int(self):
        total = 0
        prev_value = 0

        for char in reversed(self.roman):
            value = self._values[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value

        return total

    def _to_roman(self, num):
        val_roman = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]

        result = []
        for value, symbol in val_roman:
            while num >= value:
                result.append(symbol)
                num -= value
        return ''.join(result)

    def __add__(self, other):
        sum_int = self._to_int() + other._to_int()
        sum_roman = self._to_roman(sum_int)
        return Roman(sum_roman)

    def __str__(self):
        return self.roman


if __name__ == "__main__":
    r1 = Roman("XCIII")
    r2 = Roman("XIV")

    r3 = r1 + r2

    print(f"{r1} + {r2} = {r3}")

    a = Roman("II")
    b = Roman("III")
    print(f"{a} + {b} = {a + b}")
