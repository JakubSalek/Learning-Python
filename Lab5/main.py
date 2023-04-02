import math
import random


if __name__ == '__main__':
    # s = "%d %s o masie %f kilograma \n (w notacji wykładniczej) %e kilograma"
    # dane = (2, "samochody", 2364.31231245, 2334.31231)
    # print(s % dane)

    # print("*%10s*" % ("Hello"))
    # print("*%-10s*" % ("Hello"))
    # print("*%10.4f*" % (2.1251256))
    # print("*%-10.4f*" % (2.1251256))

    # s = "{1} i {0} {zwierzeta}"
    # print(s.format(2, "psy", zwierzeta="koty"))
    # s = "element listy {lista[1]} i wartosc ze slownika {slownik[b]}"
    # print(s.format(lista=(2, 3, 4), slownik={"a": "Ala", "b": "Bolek"}))

    # s = "|{0:>11s}|"
    # print(s.format("Hello"))
    # s = "|{0:<11s}|"
    # print(s.format("Hello"))
    # s = "|{0:^11s}|"
    # print(s.format("Hello"))
    # s = "|{0:*^11s}|"
    # print(s.format("Hello"))
    # s = "{0:_^20.5f}"
    # print(s.format(3.141577738))

    # x = 2
    # s1 = f"dlugosc wynosi {x}."
    # s2 = f"Pole wynosi {(x2:=x**2)}"
    # print(s1)
    # print(s2)

    # print(math.sin(math.pi/3))

    # print(random.random())
    # print(random.randint(20, 30))
    # print(random.choices("ACTG", weights=(1, 1, 1, 10), k=10))

    # try:
    #     x = 1
    #     y = 0
    #     print(x/y)
    # except ZeroDivisionError:
    #     print("Pamietaj cholero nie dziel przez zero")

    # try:
    #     x = input()
    #     print(x + 2)
    # except TypeError:
    #     print(int(x) + 2)
    # finally:
    #     print("Zrobione")

    # f = open("plik.txt", "r")
    # print(f.read())
    # print(f.tell())
    # f.seek(0)
    # print(f.readline())
    # f.seek(0)
    # for i in f:
    #     print(i, end="")
    # f.close()

    # f = open("plik.txt", "r")
    # l = filter(bool, map(lambda i: i.split("#", 1)[0].strip(), f))
    # print(list(l))
    # f.close()

    # f = open("plik.txt")
    # try:
    #     f.read()
    # finally:
    #     f.close()

    # with open("plik.txt") as f:
    #     print([i for i in f])

    # AUTOMATY AUTOMATY AUTOMATY AUTOMATY AUTOMATY AUTOMATY AUTOMATY AUTOMATY
    # rule = 90
    # predict = ["***", "**_", "*_*", "*__", "_**", "_*_", "__*", "___"]
    # prerule = ["_" * int(i == '0') + "*" * int(i == '1') for i in str(bin(rule))[2:].zfill(8)]
    # automat = {key: value for (key, value) in zip(predict, prerule)}

    # n = int(input())
    # k = int(input())
    # # cells = ["".join("_") if random.randint(0, 1) == 0 else "".join("*") for i in range(n)]     # Losowe
    # cells = "_" * (n//2) + "*" + "_" * (n//2)                         # Do trójkąta

                # LEPSZE LEPSZE LEPSZE LEPSZE LEPSZE LEPSZE LEPSZE LEPSZE LEPSZE LEPSZE
    # for i in range(k):
    #     print(cells)
    #     cells = "".join(automat.get(cells[j - 1] + cells[j] + cells[j + 1 * int(j != n-1)])
    #                     for j in range(len(cells)))
    # print(cells)

                # GORSZE GORSZE GORSZE GORSZE GORSZE GORSZE GORSZE GORSZE GORSZE GORSZE
    # print(cells)
    # for i in range(k):
    #     new_cells = ""
    #     for j in range(len(cells)):
    #         x = ""
    #         if j == 0:
    #             x = cells[-1] + cells[j] + cells[j+1]
    #         elif j == len(cells)-1:
    #             x = cells[j-1] + cells[j] + cells[0]
    #         else:
    #             x = cells[j-1] + cells[j] + cells[j+1]
    #         new_cells += automat.get(x)
    #     cells = new_cells
    #     print(cells)
