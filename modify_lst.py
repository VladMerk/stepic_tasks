lst = [1, 2, 3, 4, 5, 6]
def modify_lst(l):
    """
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
     а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка
    """
    l[:] = [i//2 for i in l if not i%2]

print(modify_lst(lst))
print(lst)
modify_lst(lst)
print(lst)

lst = [10, 5, 8, 3]
modify_lst(lst)
print(lst)