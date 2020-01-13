"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

NUM = int(input("Количество цифр? "))
b = int(input("Какое число подсчитать? "))
count = 0
for i in range(1, NUM + 1):
    m = int(input("Число " + str(i) + ": "))
    while m > 0:
        if m % 10 == b:
            count += 1
        m = m // 10

print(f"Цифра {b} встречается {count} раз ")



'Рекурсия'

NUM = int(input("Количество цифр? "))
b = int(input("Какое число подсчитать? "))

def check(m,b):
    count = 0
    if m >= 1:
         if m % 10 == b:
            count += 1
            return int(check(m // 10, b)) + count
         else:
             return int(check(m // 10, b))
    else:
        return count

def num_input (NUM,i):
    if i <= NUM:
        m = int(input("Число " + str(i) + ": "))
        return int(check(m,b)) + int(num_input (NUM,i+1))

    else:
        return 0

print(f"Цифра {b} встречается {num_input(NUM,1)} раз ")



