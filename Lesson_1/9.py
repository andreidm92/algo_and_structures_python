# 9.Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if (a < b and b < c) or (c < b and b < a):
    print (f"{b} - среднее число")
elif (b < a and a < c) or (c < a and a < b):
    print(f"{a} - среднее число")
elif (a < c and c < b) or (b < c and c < a):
    print(f"{c} - среднее число")
else:
    print ("Вы ввели одинаковые числа")
