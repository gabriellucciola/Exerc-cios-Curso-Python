lista = []
lista_par = []
lista_impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        lista_par.append(n)
    else:
        lista_impar.append(n)
    c = ''
    while c not in 'SsNN' or c == '':
        c = input('Deseja continuar? S/N: ').upper()
    if c == 'N':
        break
lista.sort()
lista_par.sort()
lista_impar.sort()
print(f'Os valores digitados foram {lista}')
print(f'Os valores pares digitados foram {lista_par}')
print(f'Os valores impares digitados foram {lista_impar}')
