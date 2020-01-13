"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

NUMB = int(input ("Введите натуральное число : "))
l = len(str(NUMB))
count = 0
for i in range(1,l+1):
    x = NUMB % 10
    if x % 2 == 0:
        count +=1
    NUMB = NUMB // 10
print (f'Четных цифр в введенном числе - {count}, нечетных - {l-count}')


''' Рекурсия '''

def toStr(n):
   count = 0
   if n < 1:
       return f'{count}'
   else:
       if  (n%10)%2 == 0:
           count +=1
           return count + int(toStr(n // 10))
       else:
           return toStr(n // 10)

NUMB = int(input ("Введите натуральное число : "))
l = len(str(NUMB))
print (f'Четных цифр в введенном числе - {toStr(NUMB)}, нечетных - {l-toStr(NUMB)}')

