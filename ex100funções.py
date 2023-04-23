from time import sleep
from random import randint

def sorteio():
    lista = []
    print('Sorteando 5 valores para a lista: ', end='')
    for i in range(0, 5):
        sleep(0.5)
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
    print('PRONTO!')
    return lista
def somaPar(lista):
    print(f'Somando os valores pares de {lista}, temos ', end='')
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(soma)


somaPar(sorteio())