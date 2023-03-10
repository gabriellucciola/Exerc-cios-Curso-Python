from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10),
         randint(0, 10), randint(0, 10))
print(f'Os números sorteados foram {tupla}')
print(f'O maior valor é {max(tupla)}')
print(f'O menor valor é {min(tupla)}')
