x = input('Digite o primeiro nome: ')
y = input('Digite o segundo nome: ')
z = input('Digite o terceiro nome: ')
w = input('Digite o quarto nome: ')
import random
s = [x, y, z, w]
print(f'O nome sorteado é: {random.choice(s)}')
