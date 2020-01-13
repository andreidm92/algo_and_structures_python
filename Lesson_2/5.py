"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""

for i in range(32, 128):
    print("{:4d}-{}".format (i, chr(i)), end='')
    if i % 10 == 0:
        print()

print()
print()

'Рекурсия'

def codes(n, m, i):
    if m-1 > n:
        i +=1
        if (i) % 10 == 0:
            return str("{:4d}-{}".format (n, chr(n))) + '\n' + str(codes(n+1,m, i))
        else:
            return str("{:4d}-{}".format(n, chr(n))) + str(codes(n + 1, m, i))
    else:
        return str("{:4d}-{}".format(m-1, chr(m-1)))



print (codes(32,128,1))