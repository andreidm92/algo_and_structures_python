"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
 который не рассматривался на уроках
"""
import timeit
import random
import statistics

def quick_sort(orig_list):
    if len(orig_list) <= 1:
        return orig_list
    else:
        q = random.choice(orig_list)
        L = []
        M = []
        R = []
        for elem in orig_list:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
        return quick_sort(L) + M + quick_sort(R)


m = int(input('Введите число для расчета размера массива: '))
orig_list = [random.randint(-100, 100) for _ in range(2*m + 1)]
sorted_array = quick_sort(orig_list) # Сортируем массив
print(f' Сгенерированный массив - {orig_list}')
print(f'Значение Медианы (модуль статистики) - {statistics.median(orig_list)}')
print(f'Значение Медианы (методом сортировки) - {sorted_array[m]}')
