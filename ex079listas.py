lista = []
while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista.append(n)
    conti = input('Deseja continuar? S/N: ')
    while conti not in 'SsNn':
        conti = input('Deseja continuar? S/N')
    if conti in 'Nn':
        break
lista.sort()
print(f'Os valores digitados foram {lista}')