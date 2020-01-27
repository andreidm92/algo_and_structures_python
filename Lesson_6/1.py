"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
import sys
import copy
from memory_profiler import profile
from guppy import hpy

# Версия Python - 3.7.4, Windows 10, разрядность - 64

''' 1. В этом примере воспользовался замерами трех функций - декоратор @profile, hpy() и getsizeof()
Выдают одинаковые результаты - оптимизация не требуется (инкремент только для декоратора).
hpy() = выдает более детальный расклад с подробной аналитикой по элементно.'''

h = hpy()
@profile

def lst_sum_cycle(num_lst):
    """Цикл"""
    total_sum = 0
    for el in num_lst:
        total_sum += el
    return total_sum


print(lst_sum_cycle([1, 3, 5, 7, 9]))
print(h.heap())
sys.getsizeof(lst_sum_cycle([1, 3, 5, 7, 9]))

''' 2. Тот же пример с рекурсией, не показал увеличения потребления памяти.
Дают результат для каждой итерации рекурсии и везде инкремент равен нулю.'''

@profile
def lst_sum_rec(num_lst):
    """Рекурсия"""
    if len(num_lst) == 1:
        return num_lst[0]
    else:
        return num_lst[0] + lst_sum_rec(num_lst[1:])


print(lst_sum_rec([1, 3, 5, 7, 9]))
sys.getsizeof(lst_sum_rec([1, 3, 5, 7, 9]))

''' 3. Для решета Эратосфена, мы также не наблюдаем увеличения потребления памяти.
       Оптимизации не требуется'''

@profile
def ert(n):
    a = [0] * n  # создание массива с n количеством элементов
    for i in range(n):  # заполнение массива ...
        a[i] = i  # значениями от 0 до n-1
    # print (a)
    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < n:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент простое число)
            while j < n:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    return b

print(ert(n = int(input("вывод простых чисел до числа ... "))))
sys.getsizeof(ert(100))