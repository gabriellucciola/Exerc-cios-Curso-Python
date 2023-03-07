n = int(input('Digite o valor que deseja ver a tabuada: '))
x = int(input('Até que valor da tabuada deseja ver? '))
print('-'*20)
for i in range(0, x+1):
    print(f'{n} x {i} = {n*i}')
print('-'*20)
