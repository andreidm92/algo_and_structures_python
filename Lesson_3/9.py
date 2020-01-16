# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

N = 5
M = 3

EXT_LST = []
for i in range(N):
    b = []
    for j in range(M):
        b.append(randint(0, 10))
        print(f"{b[j]:4d}", end='')
    EXT_LST.append(b)
    print('   |', sum(b))

for i in range(M):
    print(f" ---", end='')
print()

MIN_MIN = []
for i in range(M):
    MIN_NUMB = EXT_LST[0][i]
    for j in range(N):
        if EXT_LST[j][i] < MIN_NUMB:
            MIN_NUMB = EXT_LST[j][i]
    print(f"{MIN_NUMB:4d}", end='')
    MIN_MIN.append(MIN_NUMB)

print()
print()
print(
    f' Максимальный элемент среди минимальных элементов матрицы - {max (MIN_MIN)}')
