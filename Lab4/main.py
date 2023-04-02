from functools import reduce
from sys import argv

# def pole(*args):
#     if len(args) == 1:
#         return args[0]**2
#     elif len(args) == 2:
#         return
#     elif len(args) == 3:


if __name__ == '__main__':
    # Zadanie 8 z map
    # l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    # print(list(map(lambda x: x if x % 2 == 0 else x*2, filter(lambda x: not x % 3 == 0, l))))
    # Zadanie 9 z map
    # l = ["123", "dsads", "dsxcv", "21", "ewg"]
    # print(list(filter(lambda x: x.isalpha(), l)))
    # Zadanie 10 z map
    # l = ["123", "dsads", "dsxcv", "21", "ewg", "", " "]
    # print(list(map(lambda x: int(x), filter(lambda x: x.isnumeric(), l))))
    # Zadanie 11 z map
    # l = [(1, 2, 3, 4), (2, 3), (12, 312, 3124, 21), (), ("DSsda", "dsa", "asdd"), ('s', 's', 'd', 'b')]
    # print(list(filter(lambda x: len(x) > 2, l)))
    # Zadanie 12 z map
    # l = [(1, 2, 3), (1, 2), (5, 3), (2, 3), (10, 11), (10, 10)]
    # print(list(filter(lambda x: sum(x) % 2 == 0, l)))
    # Zadanie 13 z map
    # l = [(1, 2, 3), (1, 2), (5, 3), (2, 3), (10, 11), (10, 10), (3, 6, 9), (12, 3)]
    # print(list(filter(lambda x: , l)))

    # Od prowadzącego
    # Zadanie 8
    # l = range(1, 31)
    # l = [2 * i if i % 2 else i for i in l if i % 3]
    # print(l)
    # Zadanie 9
    # l = ["Ala", "123", "ola987"]
    # l = ["".join(i for i in j if i.isalpha()) for j in l]
    # print(l)
    # Zadanie 10
    # l = ["000", "1111", "Ala", "123", "ola987"]
    # l = [int(j) for j in ["".join(i for i in j if i.isdigit()) for j in l] if j]
    # print(l)
    # Zadanie 11
    # l = [(1, 2, 3, 4), (2, 3), (12, 312, 3124, 21), (), ("DSsda", "dsa", "asdd"), ('s', 's', 'd', 'b')]
    # l = [tuple(i[:2] for i in l if len(i) > 1)]
    # print(l)
    # Zadanie 12
    # l = [(1, 2, 3), (1, 2), (5, 3), (2, 3), (10, 11), (10, 10)]
    # l = [i for i in l if sum(i) % 2]
    # print(l)
    # Zadanie 16
    # all_items = [1, 2, 3, 4, 5]
    # cond = lambda x: x < 3
    #
    # not_all_items = not all(cond(x) for x in all_items)
    # some_not_item = any(not cond(x) for x in all_items)
    #
    # print(not_all_items == some_not_item)
    #
    # A = [True, False]
    # print(not all(A) == any(not i for i in A))
    # Zadanie 8 itakdalejitakdalej
    # l = range(1, 31)
    # print(list(map(lambda i: i * 2 if i % 2 else i, filter(lambda i: i % 3, l))))
    # Zadanie 9 z filtrami
    # l = ["Ala", "123", "ola987"]
    # print(list(map(lambda j: "".join(filter(lambda i: i.isalpha(), j)), l)))
    # Zadanie 11 z filtrami
    # l = [(1, 2, 3, 4), (2, 3), (12, 312, 3124, 21), (), ("DSsda", "dsa", "asdd"), ('s', 's', 'd', 'b')]
    # print(list(map(lambda i: tuple(i[:2]), filter(lambda i: len(i) > 1, l))))
    # Zadanie 15
    # l = ["Ala ma kota", "ola", "ma psa", "i", "kota"]
    # l = [i.split(" ", 1)[0] for i in l if " " in i]
    # print(l)
    # Zadanie 15 z listmapem
    # l = ["Ala ma kota", "ola", "ma psa", "i", "kota"]
    # l = list(map(lambda i: i.split(" ", 1)[0], filter(lambda i: " " in i, l)))
    # print(l)
    # Zadanie 24
    # l = [lambda x: x + 1, lambda x: x ** 2, lambda x: x % 3]
    # print(list(map(lambda i: i(1), filter(lambda i: i(0) == 0, l))))
