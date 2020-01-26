"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""
# 1-й вариант с namedtuple()

from collections import namedtuple

n = int(input("Количество компаний: "))
fin_result = namedtuple('fin_result', ' name per_1 per_2 per_3 per_4 ')
aver_profit = {}

for i in range(n):
    co_result = fin_result(name=input('Введите имя компании: '),
                           per_1=int(input('Введите прибыль 1-го квартала: ')),
                           per_2=int(input('Введите прибыль 1-го квартала: ')),
                           per_3=int(input('Введите прибыль 1-го квартала: ')),
                           per_4=int(input('Введите прибыль 1-го квартала: ')))

    aver_profit[co_result.name] = (co_result.per_1 + co_result.per_2 + co_result.per_3 + co_result.per_4)

aver_number = 0
for x in aver_profit.values():
    aver_number += x
aver_number = aver_number / n
print(f'Средняя прибыль всех компаний за год: {aver_number}')

for key, value in aver_profit.items():
    if value > aver_number:
        print(f'Прибыль {value} компании {key} - выше {aver_number}')
    elif value == aver_number:
        print(f'Прибыль {value} компании {key} - равна {aver_number}')
    else:
        print(f'Прибыль {value} компании {key} - ниже {aver_number}')


# 2-й вариант с defaultdict()

import collections

n_co = int(input("Введите кол-во компаний: "))

companies = collections.defaultdict()
for i in range(n_co):
    name = input(f'Введите имя {i+1}-й компании: ')
    profit = [float(input(f'Введите прибыль за {i+1} -й квартал: ')) for j in range(4)]
    companies[name] = sum(profit)
print(companies)

avr = sum(companies.values())/n_co
print(f'Средняя прибыль всех компаний за год: {avr}')

print("Компании с прибылью выше средней: ")
for c in companies:
    if companies[c] >= avr:
        print(f'{c}, {companies[c]}')

print("Компании с прибылью ниже средней: ")
for c in companies:
    if companies[c] < avr:
        print(f'{c}, {companies[c]}')
