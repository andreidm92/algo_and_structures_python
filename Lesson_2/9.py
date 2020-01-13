"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""
NUM = int(input("Количество цифр? "))
amax = 0
SUMMAX = 0
for i in range(1, NUM + 1):
    m = int(input("Число " + str(i) + ": "))
    a = m
    SUM = 0
    while m > 0:
        SUM += m % 10
        m = m // 10
    if SUM > SUMMAX:
          SUMMAX = SUM
          amax = a
print (f' Число {amax} c максимальной суммой всех цифр {SUMMAX}')
