# d1 = {'a': 1, 'b': 2}
# d2 = {'b': 3, 'c': 4}
# print(d1 != d2)


from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# print(Color.RED)        # Color.RED
# print(Color.RED.name)   # 'RED'
# print(Color.RED.value)  # 1

for c in Color:
    print(c)
    