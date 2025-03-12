import random

# Сортировка пузырьком (Bubble sort)
def bubble_sort(arr: list, *, reverse=False) -> list:
    arr = list(arr)  # Копия списка
    n = len(arr) - 1  # Количество итераций

    for i in range(n):
        swapped = False  # Проверка на обмен
        for j in range(n - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    if reverse:
        arr.reverse()

    return arr


def main():
    # Задать количество элементов списка
    n = int(input('Введите количество элементов списка: '))
    # Сформировать целочисленный список из случайных чисел
    numbers = [(random.randint(1, 99)) for _ in range(n)]
    # Вывести исходный список
    print('Исходный список:', numbers, sep='\n')
    # Отсортировать список и переприсвоить переменной списка
    numbers = bubble_sort(numbers)
    # Вывести отсортированный список
    print('Отсортированный список:', numbers, sep='\n')


if __name__ == '__main__':
    main()

