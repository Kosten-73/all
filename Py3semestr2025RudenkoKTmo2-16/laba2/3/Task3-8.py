n = int(input("Введите колличество учеников: "))

k_man, h_man = 0, 0
k_woman, h_woman = 0, 0

for i in range(n):
    height = float(input("Введите рост ученика (см): "))
    if height < 0:
        k_man += 1
        h_man += abs(height)
    else:
        k_woman += 1
        h_woman += height
h_man /= k_man
h_woman /= k_woman
all_k = k_man + k_woman
all_h = (h_man + h_woman) / 2

print(f"Количество мужчин: {k_man}, Средний рост мужчин: {h_man:.1f}, "
      f"Количество женщин: {k_woman}, Средний рост женщин: {h_woman:.1f}, "
      f"Средний рост всех учеников: {all_h:.1f}, "
      f"Количество учеников: {all_k}")

# C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\.venv\Scripts\python.exe C:\Users\korudenko\PycharmProjects\Py3semestr2025RudenkoKTmo2-16\laba2\3\Task3-8.py
# Введите колличество учеников: 5
# Введите рост ученика (см): 1321.1
# Введите рост ученика (см): -213.131232
# Введите рост ученика (см): 321
# Введите рост ученика (см): 41
# Введите рост ученика (см): 213.1231
# Количество мужчин: 1, Средний рост мужчин: 213.1, Количество женщин: 4, Средний рост женщин: 474.1, Средний рост всех учеников: 343.6, Количество учеников: 5
#
# Process finished with exit code 0
