x = int(input('Digite um número: '))
b = int(input('Digite 1 para binário, 2 para octadecimal e 3 para hexadecimal: '))
if b == 1:
    print(bin(x))
elif b == 2:
    print(oct(x))
elif b == 3:
    print(hex(x))
else:
    print('Algum valor informado é inválido, verifique e tente novamente!')
