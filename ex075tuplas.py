tupla = (int(input('Digite um valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')),
         int(input('Digite outro valor: ')))
print(f'O valor 9 aparece {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for valor in tupla:
    if valor % 2 == 0:
        print(valor, end=" ")
