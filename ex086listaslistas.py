matriz = []
matriz0 = []
matriz1 = []
matriz2 = []
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}][{j}]: '))
        if i == 0:
            matriz0.append(n)
        elif i == 1:
            matriz1.append(n)
        else:
            matriz2.append(n)
matriz.append(matriz0)
matriz.append(matriz1)
matriz.append(matriz2)
print('-='*25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {matriz[i][j]} ]', end=' ')
    print('\n', end='')
    