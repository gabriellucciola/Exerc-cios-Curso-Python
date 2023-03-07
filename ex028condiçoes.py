import random

print('Vamos jogar! Já pensei em um número entre 0 e 5, tente adivinhar!')
numrand = random.randint(0, 5)
n = int(input('Digite um valor entre 0 e 5: '))
if type(n) == int and n >=0 and n<=5:
    if n == numrand:
        print('Parabéns, você acertou!')
    else: print('Você errou, o computador venceu!')
else: print('O número digitado é inválido, execute novamente e tente outra vez.')
