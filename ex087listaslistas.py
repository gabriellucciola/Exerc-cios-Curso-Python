listas = []
soma = soma_par = soma_col2 = soma_lin1 = soma_diag_pric = 0
matriz0 = []
matriz1 = []
matriz2 = []
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para [{i}][{j}]: '))
        soma += n
        if i == 0:
            matriz0.append(n)
        if i == 1:
            matriz1.append(n)
            soma_lin1 += n
        if i == 2:
            matriz2.append(n)
        if n % 2 == 0:
            soma_par += n
        if j == 2:
            soma_col2 += n
        if i == j:
            soma_diag_pric += n
listas.append(matriz0)
listas.append(matriz1)
listas.append(matriz2)
print('-='*25)
for i in range(0, 3):
    for j in range(0, 3):
        print(f'[ {listas[i][j]} ]', end=' ')
    print('\n', end='')
print(f'A soma de todos os números é {soma}')
print(f'A soma de todos os números da coluna 2 é {soma_col2}')
print(f'A soma de todos os números da linha 1 é {soma_lin1}')
print(f'A soma da diagonal principal é {soma_diag_pric}')