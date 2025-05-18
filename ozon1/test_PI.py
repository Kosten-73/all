def bubble_sort1(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def bubble_sort(arr):
    n = len(arr)
    for i in range(1, n):
        t_i = i
        t_j = i - 1
        while arr[t_i] < arr[t_j] and t_j != -1:
            arr[t_i], arr[t_j] = arr[t_j], arr[t_i]
            t_i -= 1
            t_j -= 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Перемещаем элементы массива, которые больше key, на одну позицию вперед
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Вставляем key на правильное место в отсортированной части массива
        arr[j + 1] = key


def fact(x):
    if x == 1:
        return x
    return x * fact(x - 1)
# Пример использования
arr = [100, 1, 12, 31, 32, 0, -3, 12, 93, 1]
# insertion_sort(arr)
bubble_sort1(arr)
print("Отсортированный массив:", arr)
print(fact(5))