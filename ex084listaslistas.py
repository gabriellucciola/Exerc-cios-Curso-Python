lista = []
dados = []
maior = []
menor = []
while True:
    n = input('Nome: ')
    peso = int(input('Peso: '))
    dados.append(n)
    dados.append(peso)
    lista.append(dados[:])
    dados.clear()
    c = input('Deseja continuar? S/N: ').upper().strip()
    while c not in 'SN':
        c = input('Deseja continuar? S/N: ').upper().strip()
    if c == 'N':
        break
lista_ordenada = sorted(lista, key=lambda x: x[1])
print(f'Foram cadastradas {len(lista)} pessoas')
for k, p in enumerate(lista):
    if p[1] == lista_ordenada[0][1]:
        menor.append(p[0])
    if p[1] == lista_ordenada[-1][1]:
        maior.append(p[0])
print(f'O menor peso foi {lista_ordenada[0][1]}Kg. Peso de {menor}')
print(f'O maior peso foi {lista_ordenada[-1][1]}Kg. Peso de {maior}')
