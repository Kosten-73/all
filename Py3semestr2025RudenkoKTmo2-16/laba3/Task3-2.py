# Задача 2
import random

def split_and_sort_numbers(*args):
    return (sorted([x for x in args if x < 0], reverse=True),
            sorted([x for x in args if x >= 0]))

if __name__ == "__main__":
    print(split_and_sort_numbers(*[random.randint(-100, 100) for x in range(20)]))


# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba3\Task3-2.py
# ([-4, -9, -16, -20, -33, -36, -57, -78, -87, -87, -88], [21, 35, 59, 67, 68, 74, 80, 83, 83])
#
# Process finished with exit code 0

# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba3\Task3-2.py
# ([-18, -19, -34, -54, -62, -84], [11, 15, 17, 22, 22, 46, 48, 57, 60, 62, 65, 80, 91, 98])
#
# Process finished with exit code 0

# C:\Users\korudenko\PycharmProjects\botconfectioner\.venv2\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba3\Task3-2.py
# ([-7, -8, -8, -19, -23, -44, -46, -64, -87, -88], [5, 6, 15, 25, 39, 55, 85, 91, 93, 99])
#
# Process finished with exit code 0
