n = input('Digite um valor de 0 a 9999: ')
x = len(n)
for i in range(0,x):
    if i == 0:
        print(f'A unidade é {n[x-1]}')
    elif i == 1:
        print(f'A dezena é {n[x-2]}')
    elif i == 2:
        print(f'A Centena é {n[x-3]}')
    elif i == 3:
        print(f'O milhar é {n[0][x-4]}')
