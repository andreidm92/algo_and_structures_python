"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

L = [5, 200, 12, 100, 120, 10, 1]

a = L.index(min(L))
b = L.index(max(L))
SUM_M = 0
if b > a:
    a += 1
    for i in L[a:b]:
        SUM_M += i
    print(f' Сумма элементов составляет - {SUM_M}')
elif b < a:
    b += 1
    for i in L[b:a]:
        SUM_M += i
    print(f' Сумма элементов составляет - {SUM_M}')
else:
    print('Добавьте элементов в массив!')
