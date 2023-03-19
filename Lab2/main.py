import string

# dna = ({"A", "T"}, {"C", "G"})
# dna1 = "ATCATTGACGATGGAT"
# dna2 = "GAGTACCTCGTTCTTA"
# print(dna1)
# # for i, j in zip(dna1, dna2):
# #     if {i, j} in dna:
# #         print("|", end="")
# #     else:
# #         print(".", end="")
# # print()
# print("".join("|"*({i, j} in dna) + "."*({i, j} not in dna) for i, j in zip(dna1, dna2)))   # Nie moje ;c prowadzacego
# print("".join("|" if {i, j} in dna else "." for i, j in zip(dna1, dna2)))                   # Prawie moje, ale nie do konca
# print(dna2)

# dna1 = "ATCATTGACGATGGAT"   # T - A, C - G
# dna_dictionary = {"A": "T", "T": "A", "C": "G", "G": "C"}
# # dna2 = [dna_dictionary[elem] for elem in dna1]    # Moje
# dna2 = "".join(dna_dictionary[i] for i in dna1)     # Niemoje
# print(dna2)

# a = string.ascii_lowercase
# t = "Ala ma kota i psa.".lower()
#
# # d = dict([[i, t.count(i)] for i in a])
# # print(d)
#
# d = {}
# for letter in t:
#     if letter not in list(d.keys()) and letter in a:
#         d.update({letter: t.count(letter)})
# print(d)

### Słowniki

# d = {"a": 1, "b": 2, "c": 3}
# print(d.get("a", "Brak"))
# d["d"] = 4
# print(d)
#
# d1 = {"x": 99, "y": 100}
# d.update(d1)
# print(d)
#
# d2 = {"p": 55}
# d |= d2  # Nowszy update ;d, ale dziala od 3.9
# print(d)
#
# del d["a"]
# print(d)
#
# print(d.pop("b"))
# print(d)
#
# print(d.keys())
# print(list(d.keys()))

# d = dict([["z", 1], ["x", 2], ["y", 3]])
# print(d)

### Koniec słowników

# i = 0
# n = 30
# while (x := 2 * i + 1) < n: # Zmiennej x przypisywana jest wartość wyrażania po dwukropku
#     print(x)
#     i += 1

# k = (i**2 for i in range(10))
# print(k)        # Generator a nie Tuple
# for i in k:
#     print(i)

# l1 = [[i*j for i in range(11)] for j in range(11)]
# print(l1)

# l1 = [i*j for i in range(10) for j in range(i)]
# print(l1)

# lista = [i**2 for i in range(11) if i % 2 == 0]
# l1 = [i * 3 for i in lista]
# print(l1)

# lista = [i**2 for i in range(11) if i % 2 == 0]
# print(lista)

# n = int(input())
# for i in range(n+1):
#     print(" "*(n-i)+"*"*(2*i+1))
# for i in range(n, 0, -1):
#     print(" "*(n-i+1)+"*"*(2*i-1))

# n = int(input())
# for i in range(n):
#     for j in range(n-i):
#         print(" ", end="")
#     for j in range(i+1):
#         print("*", end="")
#     for j in range(i):
#         print("*", end="")
#     print()
# for i in range(n+1):
#     for j in range(i):
#         print(" ", end="")
#     for j in range(n-i+1):
#         print("*", end="")
#     for j in range(n-i):
#         print("*", end="")
#     print()

# i = 0
# while True:
#     print(i)
#     i += 1

# for i in range(10):
#     if i == 4:
#         # break
#         continue
#     print(i, end=" ")

# for i in range(10, 0, -2):
#     print(i, end=" ")

# s = "Ala ma kota"
# for letter in s:
#     print(letter)

# y = 1
# x = y if y>2 else 100

# x = a if b else c # Pod x wstaw a jeśli b, w przeciwnym wypadku wstaw c

# x = (True, False, True)
# print(all(x))
# print(any(x))
