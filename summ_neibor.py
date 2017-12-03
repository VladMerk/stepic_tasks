#!/usr/bin/python3
import sys
if not sys.argv[1]:
    a = str(input('Введите строку'))
    lst = []
    while a != 'end':
        lst.append([int(i) for i in a.split()])
        a = str(input('Введите строку'))
else:
    a = sys.argv[1]
    print(a)
    with open(sys.argv[1], 'r') as file:
        a = file.readlines()




# for x in range(len(lst)):
#     for y in range(len(lst[x])):
#         print(lst[x][y], end=' ')
#     print()