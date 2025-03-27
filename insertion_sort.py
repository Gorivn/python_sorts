import random

def insertion_sort(arr: list[int | float]) -> list[int | float]:
    '''Сортировка вставками'''
    arr = list(arr)
    n = len(arr)

    for i in range(1, n):
        item = arr[i]
        j = i - 1

        while j >= 0 and item < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = item

    return arr


def main():
    n = int(input('Введите количество элементов списка: '))
    numbers = [random.randint(1, 99) for _ in range(n)]
    print('Исходный список:', numbers, sep='\n')
    numbers = insertion_sort(numbers)
    print('Отсортированный список:', numbers, sep='\n')


if __name__ == "__main__":
    main()
