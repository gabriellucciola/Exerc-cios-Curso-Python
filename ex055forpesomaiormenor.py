lista = []
for i in range(0, 5):
    n = int(input('Digite o peso: '))
    lista.append(n)
lista_ordenada = sorted(lista)
print(f'O maior peso é {lista_ordenada[4]}')
print(f'O menor peso é {lista_ordenada[0]}')