c = 0
while c >= 0:
    n = int(input('Deseja ver a tabuada de que valor? '))
    if n < 0:
        break
    else:
        for i in range(1 ,11):
            print(f'{n} x {i} = {n*i}')
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
