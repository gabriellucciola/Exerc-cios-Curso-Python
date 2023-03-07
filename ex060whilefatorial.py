import math

c = 0
while c == 0:
    f = int(input('Digite um número para saber o fatorial: '))
    print(f'O fatorial de {f} é {math.factorial(f)}')
    cont = str(input('Deseja digitar outro número? S/N: ')).upper().strip()
    if cont == 'N':
        c = 1
        print('Aplicação encerrada.')
    else:
        c = 0
