#!/usr/bin/python3
"""
Напишите программу, которая считывает из файла строку, соответствующую тексту, сжатому с помощью кодирования повторов,
и производит обратную операцию, получая исходный текст.

Запишите полученный текст в файл и прикрепите его, как ответ на это задание.

В исходном тексте не встречаются цифры, так что код однозначно интерпретируем.

Sample Input:
a3b4c2e10b1

Sample Output:
aaabbbbcceeeeeeeeeeb

"""

import sys
import re

if sys.argv[1]:
    with open(sys.argv[1], 'r') as file:
        s = file.readline()
        lst = re.split('(\d+)', s)
        string = ''
        for i in range(0,len(lst)-1,2):
            string += str(lst[i]*int(lst[i+1]))
else:
    with open('data.txt', 'w') as file:
        file.write('a3b4c2e10b1')
    with open('data.txt', 'r') as file:
        s = file.readline()
        lst = re.split('(\d+)', s)
        string = ''
        for i in range(0, len(lst) - 1, 2):
            string += str(lst[i] * int(lst[i + 1]))

with open('result.txt', 'w') as f:
    f.write(string)



