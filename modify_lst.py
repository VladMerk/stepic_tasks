lst = [1, 2, 3, 4, 5, 6]
def modify_lst(l):
    """
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
     а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка
    """
    for i, value in enumerate(l):
        if value % 2 == 0:
            l[i] = l[i] // 2
        else:
            del l[i]

print(modify_lst(lst))
print(lst)
modify_lst(lst)
print(lst)
