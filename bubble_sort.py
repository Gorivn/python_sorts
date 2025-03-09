import random

# Сортировка пузырьком (Bubble sort)
def bubble_sort(arr: list) -> list:
    arr = arr[:]  # Копия списка
    n = len(arr) - 1  # Количество итераций

    for i in range(n):
        swapped = False  # Проверка на обмен
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr

# Задать количество элементов списка
n = int(input())
# Сформировать целочисленный список из случайных чисел
numbers = [(random.randint(1, 99)) for _ in range(n)]
# Вывести исходный список
print(numbers)
# Отсортировать список и переприсвоить переменной списка
numbers = bubble_sort(numbers)
# Вывести отсортированный список
print(numbers)

