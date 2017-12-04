#!/usr/bin/python3
"""
Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое
 слово в этом тексте и через пробел то, сколько раз оно встретилось. Если таких слов несколько, вывести
  лексикографически первое (можно использовать оператор < для строк).

Слова, написанные в разных регистрах, считаются одинаковыми.

Sample Input:
abc a bCd bC AbC BC BCD bcd ABC

Sample Output:
abc 3

with open('gtx.txt','r') as file:
    s = file.read().strip().lower().split()

z = {i: s.count(i) for i in s}

maximum = max(z, key=z.get)
x = {maximum: z[maximum]}

with open('gtx.txt','w') as file:
    file.write(str(x))

"""
with open('dataset_3363_3.txt', 'r') as file:
    s = file.read().replace('\n', ' ').lower().split()
    s.sort()
    d = dict()
    for i in set(s):
        d[i] = s.count(i)
    counter = max(d.values())
    for i in sorted(d):
        a = d[i]
        if a == counter:
            print(i, d[i])
            break
