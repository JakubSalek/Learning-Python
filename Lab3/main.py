from functools import reduce
from sys import argv

# parametry przed / tylko jako pozycyjne  # def concat(s1, /, s2, *, s3
# parametry za * tylko jako nazwane
# parametry miedzy / i * na oba sposoby


def concat(s1, s2='nie ma', s3='nic'):
    return s1 + " " + s2 + " " + s3


def dlugosc(x):
    if type(x) in (str, list, tuple, bytes):
        return len(x)
    elif type(x) in (int, float, complex):
        return abs(x)
    else:
        return type(x)


def f(*args):
    # print(args)
    for i in args:
        print(i)
    print(len(args))


def f2(*args, **kwargs):
    """To jest moja funkcja"""
    print(args)
    print(kwargs)


def f3(x):
    i = x - 1  # lokalnie zmienia wartosc
    print(i)
    return x ** i


def f4(x):
    global i
    i = x + 2  # Tu juz zmieniamy globalnie zmienna
    print(i)
    return x ** i


if __name__ == '__main__':
    # print(concat("Ala"))
    # print(concat("Ola", "nie wie"))
    # print(concat("Ala", s3="kota"))

    ################################

    # print(dlugosc(1))

    ##############################

    # f(1, 2.3, 'h', "Witam", [10, 12], (1111, 111))

    ################################

    # f2(1, 2.3, 'h', "Hello", a=3, c=10)  # parametry z nazwą są dodawane do słownika w funkcji

    ################################

    # print("A".split.__doc__)
    # print(f2.__doc__)

    ##############################

    # i = 3
    # print(f3(3))
    # print(i)

    #############################

    # i = 3
    # print(f4(3))
    # print(i)

    ###########################

    # szescian = lambda x: x**3
    # print(szescian(5))
    # funkcja = lambda a, b, c=2: (a+b)**c
    # print(funkcja(1, 2))

    ###########################

    # f = lambda *args: args[len(args)-1] if args else None
    # print(f(1, 2, ["a"]))
    # print(f())

    ############################

    # sz = lambda x: x**3
    # l = [1, 2, 3]
    # m = map(sz, l)
    # print(list(m))  # Trzeba zrzutować
    # print(list(map(lambda x: x % 2, [1, 2, 3, 4])))

    ############################

    # select = lambda x: x > 0
    # l = [1, -2, 3, -4, 5, -6]
    # print(list(filter(select, l)))

    #############################

    # l = ["a", "b", "c", "d"]
    # def f(x, y):
    #     print("arguments: ", x, y)
    #     return x + y
    # print(reduce(f, l)) # bierze element z poprzedniego wykonania
    #                     # jako pierwszy argument a drugi to element z listy

    ##########################

    # n = 3
    # print(reduce(lambda x, y: x*y, range(1, n+1)))

    ##########################

    # l = [1, 7, 3, 5, 8, 2, 5, 0]
    # print(sorted(l, key=lambda e: e % 2))
    # s = ["ala", "alz", "ola", "pies", "drzewo", "lokomotywa"]
    # print(sorted(s, key=lambda e: len(e)))

    # ZADANIE # ZADANIE # ZADANIE # ZADANIE # ZADANIE # ZADANIE # ZADANIE
    
    # a = [5, 4, 3, 2, 1]
    # b = [1, 2, 3, 4, 5]
    # def iloczyn_skalarny(a: [], b: []):
    #     result = 0
    #     for i in range(len(a)):
    #         result += a[i]*b[i]
    #     return result
    # print(iloczyn_skalarny(a, b))
    # def il_sk(a, b):    # sumowanie wartosci z krotki
    #     return sum(map(lambda i: i[0]*i[1], zip(a, b)))
    # print(il_sk(a, b))
    # d = {"a": 3, "b": 1, "c": 2}
    # print(sorted(d, key=lambda x: d.get(x)))
    # s = [4, 5, 2, 3]
    # print(reduce(lambda x, y: x*10 + y, s))
    # x = input("Podaj liczbe: ")
    # print(x)
    # print(argv) # Argumenty przy wywołaniu funkcji

    # Zadanie z automatami komórkowymi
    predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
    rule = 31
    symbolic_rule = ["*" if i == '1' else "_" for i in bin(rule)[2:].zfill(8)]
    print(symbolic_rule)
    d = {key: value for (key, value) in zip(predict, symbolic_rule)}
    print(d)

    pass
