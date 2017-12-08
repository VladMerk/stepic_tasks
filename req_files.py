"""
Имеется набор файлов, каждый из которых, кроме последнего, содержит имя следующего файла.
Первое слово в тексте последнего файла: "We".

Скачайте предложенный файл. В нём содержится ссылка на первый файл из этого набора.

Все файлы располагаются в каталоге по адресу:
https://stepic.org/media/attachments/course67/3.6.3/

Загрузите содержимое ﻿последнего файла из набора, как ответ на это задание.

"""

import requests

def req_lines(url, num):
    num += 1
    link = 'https://stepic.org/media/attachments/course67/3.6.3/'
    link = link+str(url)
    print(link)
    r = requests.get(link)
    line = r.text
    print(line)
    print(num)
    if 'We' not in line:
        req_lines(line, num)
    else:
        with open('result.txt', 'w') as file:
            file.write(line)

link = ''
with open('dataset_3378_3.txt') as file:
    url = file.readline().split('/')
    url = url[-1].strip()
    req_lines(url, 0)

