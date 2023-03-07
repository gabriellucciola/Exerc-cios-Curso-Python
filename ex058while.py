import random

print('Vamos começar o jogo de adivinhação')
valor = random.randint(0, 10)
c = 0
palpite = -1
while palpite != valor:
    c += 1
    palpite = int(input(f'Tentativa {c}: '))
    if palpite != valor:
        print('Você errou, tente novamente!')
print(f'Você venceu com {c} tentativas, parabens!')
