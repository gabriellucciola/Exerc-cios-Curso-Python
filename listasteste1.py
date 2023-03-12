lista = [7, 8, 2, 16, 12]
print(len(lista), max(lista))
lista.append(8)
lista.insert(3, 41)
lista.sort()
del lista[-2]
print(lista, len(lista), max(lista))
lista1 = list(range(7, 16))
print(lista1, len(lista1))