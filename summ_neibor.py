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
    with open(sys.argv[1], 'r') as file:
        a = file.readlines()

