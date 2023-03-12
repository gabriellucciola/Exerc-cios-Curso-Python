lista_num = []
for i in range(0, 5):
    num = int(input(f'Digite um número para a posição {i}: '))
    lista_num.append(num)
print('-='*30)
print(f' Você digitou os valores {lista_num}')
print(f'O maior valor digitado foi {max(lista_num)} nas posições ', end='')
for c, n in enumerate(lista_num):
    if n == max((lista_num)):
        print(c, end='... ')
print(f'\nO menor falor digitado foi {min(lista_num)} nas posições ', end='')
for c, n in enumerate(lista_num):
    if n == min(lista_num):
        print(c, end='... ')
