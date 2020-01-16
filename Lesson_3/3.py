# 3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

from random import randint

N = int(input('Введите размер массива: '))
B = []
for j in range(N):
    x = randint(-100, 100)
    B.append(x)
print(B)
i = B.index(min(B))
k = B.index(max(B))
B[i], B[k] = B[k], B[i]
print(B)
