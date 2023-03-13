lista = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    c = ''
    while c not in 'SsNn' or c == '':
        c = input('Defeja continuar? S/N: ').upper()
    if c == 'N':
        break
print(f'Foram digitados {len(lista)} valores')
lista.sort(reverse = True)
print(f'Valores digitados em ordem decrescente {lista}')
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')