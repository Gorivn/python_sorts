import random

def selection_sort(arr: list[int | float]) -> list[int | float]:
    '''Сортировка выбором'''
    arr = list(arr)
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def main():
    n = int(input('Введите количество элементов списка: '))
    numbers = [random.randint(1, 99) for _ in range(n)]
    print('Исходный список:', numbers, sep='\n')
    numbers = selection_sort(numbers)
    print('Отсортированный список', numbers, sep='\n')


if __name__ == '__main__':
    main()