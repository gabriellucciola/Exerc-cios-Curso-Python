lista = [-1] * 6
for i in range(0, 5):
    num = int(input('Digite um número: '))
    for j in range(0, 5):
        if num <= lista[j] or lista[j] == -1:
            lista.insert(j, num)
            if -1 in lista:
                lista.remove(-1)
            break
    if lista[j+1] == -1:
        print('Adicionado ao final da lista...')
    else:
        print(f'Adicionado na posição {j} da lista...')
lista.remove(-1)
print(f'Os valores digitados em ordem foram {lista}')
